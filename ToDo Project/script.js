const taskEnter = document.getElementById("taskenter");
const taskBorder = document.getElementById('task-border');
const BtnAdd = document.querySelector(".btn");
BtnAdd.addEventListener("click", newTask);

function newTask() {
    if (taskEnter.value != '') {
    let newItem = document.createElement("li");
    // newItem.addEventListener("dblclick", editTask);
    newItem.innerHTML = taskEnter.value;
    taskBorder.appendChild(newItem);
    let span = document.createElement("span");
    span.innerHTML = "\u00d7";
    newItem.appendChild(span)
    taskEnter.value = '';
    save();
    }
}

// function editTask(event) {
//     let item = event.target.innerHTML;
//     let newInput = document.createElement('input');
//     newInput.type = 'text';
//     newInput.value = item;
//     newInput.addEventListener('keypress', saveTask);
//     newInput.addEventListener('click', saveTask);
//     event.target.parentNode.prepend(newInput);
//     event.target.remove();
//     newInput.select();
// }

// function saveTask(event) {
//     let inputVal = event.target.value;
//     if (event.target.value.length > 0 && (event.keyCode === 13 || event.type === 'click')) {
//         let newLi = document.createElement('li');
//         newLi.addEventListener('click', toggleDone);
//         newLi.addEventListener('dblclick', editTask);
//         newLi.textContent = event.target.value;
//         event.target.parentNode.prepend(li);
//         event.target.remove();
//     }
// }
window.addEventListener('keydown', function(prs) {
    if(prs.key === 'Enter' && taskEnter.value != '') {
    newTask();
    }
}, false);


taskBorder.addEventListener("click", function(call) {
    if(call.target.tagName === "LI") {
        call.target.classList.toggle("check");
    }
    
    else if(call.target.tagName === "SPAN") {
        call.target.parentElement.remove();
    }
    save();
}, false);

function save() {
    localStorage.setItem("data", taskBorder.innerHTML);
}

function show() {
    taskBorder.innerHTML = localStorage.getItem("data");
}
show();
