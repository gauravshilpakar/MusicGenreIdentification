

const button = document.getElementById("button")
const audio = document.getElementById("player")
const uploadmessage = document.querySelector("#uploadmessage")
const fileform = document.getElementById("fileform")

const upload = (file) => {
    const data = new FormData()
    data.append('audiofile', file)

    fetch('http://localhost:5000/fileupload', {
        method: 'POST',
        body: data
    }).catch(error => console.log(error))
    uploadmessage.textContent = "Upload Successfull!!"
}

fileform.addEventListener('submit', (e) => {
    e.preventDefault()
    const audiofile = document.getElementById("file")
    upload(audiofile.files[0])
})


// const filegetter = (filename) => {
//     data = filename
//     fetch('http://localhost:5000/viewfile', {
//         method: 'GET',
//         body: data
//     }).then(())
// }



// const searchquery = document.querySelector('form')
// const input = document.querySelector('input')

// searchquery.addEventListener('submit', (e) => {
//     fetch("https://google.com/search?q=" + input.value).then((response) => {

//     })
// })


// var record = false
// button.addEventListener('click', () => {
//     if (button.innerText == 'start') {
//         button.innerText = 'stop'
//         record = true
//         navigator.mediaDevices.getUserMedia({ audio: true, video: false }).then(recordAudio);
//     } else {
//         button.innerText = 'start'
//         recordAudio.stop()
//     }
// })


// const recordAudio = async (stream) => {
//     chunks = []
//     const mediaRecorder = new MediaRecorder(stream)
//     mediaRecorder.addEventListener('dataavailable', (ev) => {
//         chunks.push(ev.data)
//     })

//     mediaRecorder.addEventListener('stop', function () {
//         const blob = new Blob(chunks);
//         const audioUrl = URL.createObjectURL(blob);
//         const audio = new Audio(audioUrl);
//         if (window.URL) {
//             player.srcObject = audio;
//         } else {
//             player.src = blob;
//         }

//     })

//     const stop = () => {
//         mediaRecorder.stop()
//     }
// }