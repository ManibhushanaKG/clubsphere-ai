import Upload from "./components/Upload";

import Chat from "./components/Chat";

export default function App() {

    return (

        <div
            style={{
                minHeight: "100vh",
                background: "#111827",
                color: "white",
                padding: 40,
                fontFamily: "Arial",
            }}
        >

            <h1>🤖 ClubSphere AI</h1>

            <p>

                Intelligent Club Knowledge Assistant

            </p>

            <Upload />

            <Chat />

        </div>

    );

}