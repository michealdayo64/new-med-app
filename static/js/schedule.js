//var allTab = [...document.getElementsByClassName("tab")];
const btn_trial = document.getElementById("btn-trial");
const service = document.getElementById("service");
const dateandtime = document.getElementById("dateandtime");
const datetime_panel = document.querySelector(".datetime-panel");
const t1 = document.getElementById("t1");
const t2 = document.getElementById("t2");
const t3 = document.getElementById("t3")
const active2 = document.getElementsByClassName("active2");
const alert = document.getElementsByClassName("mycar-aler")[0];
const sec_back = document.getElementById("sec-back");
var bb = document.getElementsByClassName("bb")
var select_time = document.getElementsByClassName("select-time")
const basic_detail = document.getElementById("basicdetail")
const basicdetail_content = document.querySelector(".basicdetail-content")
const date_picker_ele = document.querySelector(".date-picker-wrapper");
const selected_date_ele = document.querySelector(" .selected-date");
const dates_ele = document.querySelector(".dates-container");
const month_ele = document.querySelector(".month .month-item");
const next_month_ele = document.querySelector(".month .next-month");
const prev_month_ele = document.querySelector(".month .prev-month");
const days_ele = document.querySelector(".days-container");



function trialBTN() {
  service.style.display = "none";
  btn_trial.style.display = "none";
  dateandtime.style.display = "block";
  datetime_panel.style.display = "flex";
  t1.classList.remove("active1");
  t2.classList.add("active2");
  sec_back.style.display = "block";
  date_picker_ele.style.display = "block"
  alert.style.display = "none";
}

btn_trial.addEventListener("click", trialBTN);

t2.addEventListener("click", () => {
  alert.style.display = "flex";
});

sec_back.addEventListener("click", () => {
  service.style.display = "block";
  btn_trial.style.display = "block";
  dateandtime.style.display = "none";
  datetime_panel.style.display = "none"
  t1.classList.add("active1");
  t2.classList.remove("active2");
  sec_back.style.display = "none";
  alert.style.display = "none";
});


  function selectTime(timeId){
    const valuu = document.getElementById(timeId).textContent
    console.log(valuu)
    dateandtime.style.display = "none";
    datetime_panel.style.display = "none";
    t1.classList.remove("active1");
    t2.classList.remove("active2");
    t3.classList.add("active3")
    sec_back.style.display = "block";
    basic_detail.style.display = "block"
    basicdetail_content.style.display = "block"
  }
    
  

// CALENDAR CODE

const months = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
];

let date = new Date();
let day = date.getDate();
let month = date.getMonth();
let year = date.getFullYear();

let selectedDate = date;
let selectedDay = day;
let selectedMonth = month;
let selectedYear = year;

month_ele.textContent = months[month] + " " + year;

selected_date_ele.textContent = formatDate(date);
selected_date_ele.dataset.value = selectedDate;

populateDates();

//date_picker_ele.addEventListener("click", toggleDatePicker);
next_month_ele.addEventListener("click", goToNextMonth);
prev_month_ele.addEventListener("click", goToPrevMonth);

/*function toggleDatePicker(e) {
  if (!checkClassExist(e.path, "dates-container")) {
    dates_ele.classList.toggle("active");
  }
}*/

function checkClassExist(path, selector) {
  if (path !== undefined) {
    for (let i = 0; i < path.length; i++) {
      if (path[i].classList && path[i].classList.contains(selector)) {
        return true;
      }
    }
  }
  return false;
}

function goToNextMonth() {
  month++;
  if (month > 11) {
    month = 0;
    year++;
  }
  month_ele.textContent = months[month] + " " + year;
  populateDates();
}

function goToPrevMonth() {
  month--;
  if (month < 0) {
    month = 11;
    year--;
  }
  month_ele.textContent = months[month] + " " + year;
  populateDates();
}

function populateDates() {
  days_ele.innerHTML = "";
  let total_days;

  if (month == 1) {
    total_days = 28;
  } else if (month % 2 === 0) {
    total_days = 31;
  } else {
    total_days = 30;
  }

  for (let i = 0; i < total_days; i++) {
    const day_element = document.createElement("div");
    day_element.classList.add("day");
    day_element.textContent = i + 1;

    if (
      selectedDay == i + 1 &&
      selectedYear == year &&
      selectedMonth == month
    ) {
      day_element.classList.add("selected");
    }

    day_element.addEventListener("click", function () {
      selectedDate = new Date(year + "-" + (month + 1) + "-" + (i + 1));
      selectedDay = i + 1;
      console.log(selectedDay)
      selectedMonth = month;
      selectedYear = year;

      selected_date_ele.textContent = formatDate(selectedDate);
      selected_date_ele.dataset.value = selectedDate;
    });

    days_ele.appendChild(day_element);
  }
}

function formatDate(selectedDate) {
  let day = selectedDate.getDate();
  if (day < 10) {
    day = "0" + day;
  }

  let month = selectedDate.getMonth() + 1;
  if (month < 10) {
    month = "0" + month;
  }

  let year = selectedDate.getFullYear();

  return day + " / " + month + " / " + year;
}



