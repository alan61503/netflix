const express = require("express");
const mongoose = require("mongoose");
const bcrypt = require("bcrypt");
const cors = require("cors");
const jwt = require("jsonwebtoken");
require("dotenv").config();

const app = express();
app.use(express.json());
app.use(cors());

// Connect to MongoDB Atlas
mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log("✅ Connected to MongoDB Atlas"))
    .catch(err => console.error("❌ MongoDB Connection Error:", err));

// User Schema
const User = mongoose.model("User", new mongoose.Schema({
    email: String,
    password: String,
    name: String
}));

// Signup Route
app.post("/signup", async (req, res) => {
    const { email, password, name } = req.body;
    const hashedPassword = await bcrypt.hash(password, 10);
    try {
        await User.create({ email, password: hashedPassword, name });
        res.json({ message: "User registered successfully!" });
    } catch (err) {
        res.status(500).json({ error: "Error registering user" });
    }
});

// Login Route
app.post("/login", async (req, res) => {
    const { email, password } = req.body;
    const user = await User.findOne({ email });
    if (!user) return res.status(400).json({ error: "User not found" });

    const validPassword = await bcrypt.compare(password, user.password);
    if (!validPassword) return res.status(400).json({ error: "Invalid credentials" });

    const token = jwt.sign({ id: user._id }, "secretkey", { expiresIn: "1h" });
    res.json({ message: "Login successful!", token });
});

// Start Server
app.listen(5000, () => console.log("🚀 Server running on port 5000"));
