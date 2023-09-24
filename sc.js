
document.addEventListener("DOMContentLoaded", function () {
   
    const commentTextArea = document.getElementById("comment");
    const reviewButton = document.getElementById("review-button");
    const resultDiv = document.getElementById("output");


    reviewButton.addEventListener("click", function () {
        
        const commentText = commentTextArea.value;

        
        fetch("/finalmodel", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ data: commentText }),
        })
            .then((response) => response.json())
            .then((data) => {
                
                resultDiv.innerHTML = `Sentiment: ${data.sentiment}`;
            })
            .catch((error) => {
                console.error("Error:", error);
                resultDiv.innerHTML = "Error occurred.";
            });
    });
});