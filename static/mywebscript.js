let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("POST", "/emotionDetector", true); // Change to POST
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"); // Set header
    xhttp.send("text=" + encodeURIComponent(textToAnalyze)); // Send data in body
};