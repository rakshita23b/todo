
/* =========================
   GET HTML ELEMENTS
========================= */

const taskInput = document.getElementById("taskInput");
const addBtn = document.getElementById("addBtn");
const taskList = document.getElementById("taskList");

const taskCount = document.getElementById("taskCount");
const completedCount = document.getElementById("completedCount");
const pendingCount = document.getElementById("pendingCount");
const taskLabel = document.getElementById("taskLabel");


/* =========================
   LOAD TASKS FROM STORAGE
========================= */

let tasks = [];

try {
    tasks = JSON.parse(localStorage.getItem("myTasks")) || [];
} catch (error) {
    console.error("Could not load saved tasks:", error);
    tasks = [];
}


/* =========================
   SAVE TASKS
========================= */

function saveTasks() {

    localStorage.setItem("myTasks", JSON.stringify(tasks));

}


/* =========================
   CREATE - ADD TASK
========================= */

function addTask() {

    const taskText = taskInput.value.trim();

    if (taskText === "") {

        alert("Please enter a task!");

        return;
    }

    const task = {

        id: Date.now(),

        text: taskText,

        completed: false

    };

    tasks.push(task);

    saveTasks();

    taskInput.value = "";

    displayTasks();

}


/* =========================
   READ - DISPLAY TASKS
========================= */

function displayTasks() {

    taskList.innerHTML = "";

    if (tasks.length === 0) {

        const emptyMessage = document.createElement("li");

        emptyMessage.className = "empty-message";

        emptyMessage.textContent = "No tasks yet. Add your first task!";

        taskList.appendChild(emptyMessage);

    }


    tasks.forEach((task) => {

        const li = document.createElement("li");

        li.className = "task-item";


        // CHECKBOX

        const checkbox = document.createElement("input");

        checkbox.type = "checkbox";

        checkbox.className = "task-checkbox";

        checkbox.checked = task.completed;


        // TASK TEXT

        const span = document.createElement("span");

        span.className = "task-text";

        span.textContent = task.text;


        if (task.completed) {

            span.classList.add("completed");

        }


        // MARK AS COMPLETED

        checkbox.addEventListener("change", () => {

            task.completed = checkbox.checked;

            saveTasks();

            displayTasks();

        });


        // EDIT BUTTON

        const editBtn = document.createElement("button");

        editBtn.textContent = "Edit";

        editBtn.className = "edit-btn";

        editBtn.type = "button";


        editBtn.addEventListener("click", () => {

            updateTask(task.id);

        });


        // DELETE BUTTON

        const deleteBtn = document.createElement("button");

        deleteBtn.textContent = "Delete";

        deleteBtn.className = "delete-btn";

        deleteBtn.type = "button";


        deleteBtn.addEventListener("click", () => {

            deleteTask(task.id);

        });


        // ADD ELEMENTS TO LIST

        li.appendChild(checkbox);

        li.appendChild(span);

        li.appendChild(editBtn);

        li.appendChild(deleteBtn);

        taskList.appendChild(li);

    });


    updateCounters();

}


/* =========================
   UPDATE - EDIT TASK
========================= */

function updateTask(id) {

    const task = tasks.find((t) => t.id === id);

    if (!task) {
        return;
    }

    const newText = prompt("Edit your task:", task.text);

    if (newText === null) {
        return;
    }

    if (newText.trim() === "") {

        alert("Task cannot be empty!");

        return;
    }

    task.text = newText.trim();

    saveTasks();

    displayTasks();

}


/* =========================
   DELETE - REMOVE TASK
========================= */

function deleteTask(id) {

    const confirmDelete = confirm("Are you sure you want to delete this task?");

    if (!confirmDelete) {
        return;
    }

    tasks = tasks.filter((task) => task.id !== id);

    saveTasks();

    displayTasks();

}


/* =========================
   UPDATE TASK COUNTERS
========================= */

function updateCounters() {

    const total = tasks.length;

    const completed = tasks.filter(
        (task) => task.completed
    ).length;

    const pending = total - completed;


    taskCount.textContent = total;

    completedCount.textContent = completed;

    pendingCount.textContent = pending;


    taskLabel.textContent =
        total + (total === 1 ? " task" : " tasks");

}


/* =========================
   BUTTON CLICK EVENT
========================= */

addBtn.addEventListener("click", addTask);


/* =========================
   ENTER KEY EVENT
========================= */

taskInput.addEventListener("keydown", (event) => {

    if (event.key === "Enter") {

        addTask();

    }

});


/* =========================
   INITIAL DISPLAY
========================= */

displayTasks();

