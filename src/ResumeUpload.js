import React, { useState } from "react";
import axios from "axios";
import "./ResumeUpload.css";

function ResumeUpload({ setResult }) {
  const [file, setFile] = useState(null);
  const [role, setRole] = useState("");

  const handleSubmit = async () => {
    if (!file || !role) {
      alert("Please upload resume and select role");
      return;
    }

    const formData = new FormData();
    formData.append("resume", file);
    formData.append("role", role);

    try {
      const response = await axios.post(
        "http://localhost:5000/analyze",
        formData
      );
      setResult(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="upload-container">
      <h3>Upload Resume</h3>

      <input type="file" onChange={(e) => setFile(e.target.files[0])} />

      <select onChange={(e) => setRole(e.target.value)}>
        <option value="">Select Job Role</option>
        <option value="Frontend Developer">Frontend Developer</option>
        <option value="Backend Developer">Backend Developer</option>
        <option value="Data Scientist">Data Scientist</option>
        <option value="AI Engineer">AI Engineer</option>
      </select>

      <button onClick={handleSubmit}>Analyze Resume</button>
    </div>
  );
}

export default ResumeUpload;
