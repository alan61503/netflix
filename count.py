import cv2

input_video =r"people.mp4"

def vid_inf(vid_path):
    # Create a VideoCapture object
    cap = cv2.VideoCapture(vid_path)

    if not cap.isOpened():
        print(f"Error opening video file: {vid_path}")
        return

    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_size = (frame_width, frame_height)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    output_video = "output_recorded.mp4"
    out = cv2.VideoWriter(output_video, fourcc, fps, frame_size)

    # Create Background Subtractor MOG2 object
    backSub = cv2.createBackgroundSubtractorMOG2()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Error reading frame")
            break

        # Apply background subtraction
        fg_mask = backSub.apply(frame)

        # Apply global threshold to remove shadows
        retval, mask_thresh = cv2.threshold(fg_mask, 180, 255, cv2.THRESH_BINARY)

        # Apply morphological operations
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        mask_eroded = cv2.morphologyEx(mask_thresh, cv2.MORPH_OPEN, kernel)

        # Find contours
        contours, _ = cv2.findContours(mask_eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        min_contour_area = 500
        large_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]

        frame_out = frame.copy()
        for idx, cnt in enumerate(large_contours):
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame_out, (x, y), (x + w, y + h), (0, 0, 200), 3)
            cv2.putText(frame_out, f'#{idx+1}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Display the total number of People on the frame
        total_boxes = len(large_contours)
        cv2.putText(frame_out, f'Total People: {total_boxes}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # Write the frame into the file 'output_video'
        out.write(frame_out)

        # Display the resulting frame
        cv2.imshow("Frame_final", frame_out)

        # Check for key press
        key = cv2.waitKey(30) & 0xFF
        if key == ord("q") or key == 27:  # 'q' or 'Esc' key
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Call the function with the video path
vid_inf(input_video)
