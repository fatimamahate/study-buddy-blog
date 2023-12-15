// const updateButtons = document.getElementsByClassName("btn-edit");
// const commentBody = document.getElementById("id_body");
// const commentForm = document.getElementById("commentForm");
// const postComment = document.getElementById("postComment");

// for (let button of updateButtons) {
//     button.addEventListener("click", (e) => {
//         let commentId = e.target.getAttribute("comment_id");
//         let commentContent = document.getElementById(`comment${commentId}`).innerText;
//         commentBody.value = commentContent;
//         postComment.innerText = "Update";
//         commentForm.setAttribute("action", `edit_comment/${commentId}`);
//     });
// }