import { useState } from "react";
import { uploadPDF } from "../services/api";

export default function Upload() {
    const [file, setFile] = useState(null);
    const [status, setStatus] = useState("");
    const [loading, setLoading] = useState(false);

    async function upload() {
        if (!file) return;

        setLoading(true);
        setStatus("");

        try {
            await uploadPDF(file);
            setStatus("✅ Upload Complete");
        } catch (err) {
            setStatus("❌ Upload Failed");
        }

        setLoading(false);
    }

    return (
        <div style={{ marginBottom: 30 }}>

            <input
                type="file"
                accept=".pdf"
                onChange={(e) => setFile(e.target.files[0])}
            />

            <button
                onClick={upload}
                disabled={loading}
                style={{
                    marginLeft: 10,
                    padding: "8px 18px",
                    cursor: "pointer"
                }}
            >
                {loading ? "Uploading..." : "Upload"}
            </button>

            {file && (
                <div style={{ marginTop: 15 }}>
                    📄 <b>{file.name}</b>
                </div>
            )}

            {status && (
                <div
                    style={{
                        marginTop: 10,
                        color: "#22c55e"
                    }}
                >
                    {status}
                </div>
            )}

        </div>
    );
}