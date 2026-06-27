export default function Message({ role, text, sources }) {

    return (

        <div
            style={{
                display: "flex",
                justifyContent:
                    role === "user"
                        ? "flex-end"
                        : "flex-start",
                marginBottom: 15,
            }}
        >

            <div
                style={{
                    background:
                        role === "user"
                            ? "#2563eb"
                            : "#374151",

                    color: "white",

                    padding: 15,

                    borderRadius: 12,

                    maxWidth: "70%",
                }}
            >

                <div>{text}</div>

                {role === "bot" && sources && sources.length > 0 && (

                    <div
                        style={{
                            marginTop: 12,
                            paddingTop: 10,
                            borderTop: "1px solid rgba(255,255,255,0.2)",
                            fontSize: 14,
                            color: "#d1d5db",
                        }}
                    >

                        <strong>📄 Source</strong>

                        <ul
                            style={{
                                marginTop: 6,
                                paddingLeft: 20,
                            }}
                        >
                            {sources.map((source, index) => (
                                <li key={index}>{source}</li>
                            ))}
                        </ul>

                    </div>

                )}

            </div>

        </div>

    );
}