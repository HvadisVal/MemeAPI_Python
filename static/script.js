const API_BASE = "http://127.0.0.1:8000/api";

async function fetchMemes() {
    let response = await fetch(`${API_BASE}/memes`);
    let memes = await response.json();
    
    let memeList = document.getElementById("meme-list");
    memeList.innerHTML = "";
    
    memes.forEach(meme => {
        let div = document.createElement("div");
        div.innerHTML = `<h3>${meme.title}</h3>
                         <img src="${meme.imageUrl}" width="200">
                         <p>${meme.description}</p>
                         <button onclick="voteMeme('${meme._id}')">Vote</button>
                         <button onclick="deleteMeme('${meme._id}')">Delete</button>`;
        memeList.appendChild(div);
    });
}

async function addMeme() {
    let title = document.getElementById("meme-title").value;
    let imageUrl = document.getElementById("meme-url").value;
    let description = document.getElementById("meme-description").value;

    await fetch(`${API_BASE}/memes`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, imageUrl, description, creator: "user123" })
    });

    fetchMemes();
}
