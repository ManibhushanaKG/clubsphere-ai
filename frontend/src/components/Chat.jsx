import { useState } from "react";

import Message from "./Message";

import { askQuestion } from "../services/api";

export default function Chat() {

    const [messages, setMessages] = useState([]);

    const [question, setQuestion] = useState("");
    const [loading, setLoading] = useState(false);

    async function send() {

        if (!question.trim()) return;

        const userMessage = {
            role: "user",
            text: question,
        };

        setMessages(prev => [...prev, userMessage]);

        const q = question;

        setQuestion("");

        setLoading(true);

const response = await askQuestion(q);

setLoading(false);

setMessages(prev => [
    ...prev,
    {
        role: "bot",
        text: response.reply,
        sources: response.sources
    },
]);

    }

    return (

        <div>

            <div
                style={{
                    height: 500,
                    overflowY: "auto",
                    background: "#1f2937",
                    padding: 20,
                    borderRadius: 10,
                }}
            >

                {messages.map((m, i) => (

                    <Message
    key={i}
    role={m.role}
    text={m.text}
    sources={m.sources}
/>

                ))}
                {loading && (
    <Message
        role="bot"
        text="🤖 Thinking..."
    />
)}

            </div>

            <div
                style={{
                    display: "flex",
                    marginTop: 20,
                }}
            >

               <input
    value={question}
    onChange={(e) => setQuestion(e.target.value)}

    onKeyDown={(e) => {
        if (e.key === "Enter") {
            send();
        }
    }}

    placeholder="Ask something..."

    style={{
        flex: 1,
        padding: 15,
        fontSize: 16,
    }}
/>

                <button
    onClick={send}
    disabled={loading}
    style={{
        width: 120,
        cursor: "pointer"
    }}
>
    {loading ? "..." : "Send"}
</button>

            </div>

        </div>

    );
}