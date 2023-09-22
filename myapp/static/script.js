// Update the URL to fetch JSON data from your Django view
const jsonDataUrl = '/enigma404/play_latest_audio/';

// Get the audio player element
const audioPlayer = document.getElementById('audioPlayer');

// Send a POST request to the Django view
fetch(jsonDataUrl, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ audio_data: audioData }), // Replace 'audioData' with your actual audio data
})
    .then(response => {
        if (response.status === 200) {
            return response.blob();
        } else {
            throw new Error('Failed to fetch audio data');
        }
    })
    .then(audioBlob => {
        // Create a URL for the Blob
        const audioUrl = URL.createObjectURL(audioBlob);

        // Set the audio source to the created URL
        audioPlayer.src = audioUrl;

        // Start playing the audio
        audioPlayer.play();
    })
    .catch(error => {
        console.error('Error fetching and playing audio data:', error);
    });
