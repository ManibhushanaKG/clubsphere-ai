const API = "http://127.0.0.1:8000";

export async function askQuestion(question) {
    const res = await fetch(
        `${API}/chat?prompt=${encodeURIComponent(question)}`
    );

    return await res.json();
}

export async function uploadPDF(file) {

    const form = new FormData();

    form.append("file", file);

    const res = await fetch(`${API}/upload`, {
        method: "POST",
        body: form,
    });

    return await res.json();
}