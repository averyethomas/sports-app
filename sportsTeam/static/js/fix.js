var jobTitleA = ["Architects"];
var jobCatBigA = ["Architecture and Engineering"];
var A_PCT10A = [44930];
var A_PCT25A = [57620];
var A_MDA = [74110];
var A_PCT75A = [94120];
var A_PCT90A = [119370];
var totEmpA = ["84,210"];
var entryEdA = ["Bachelor's Degree"];
var workExpA = ["None"];
var pctGrowA = [17.3];
var aMeanA = ["79,650"];
var hMeanA = ["38.29"];

$( document ).ready(function() {
    loadData
    document.getElementById('#job-title-p').innerHTML = jobTitleA;
    document.getElementById('#total-p').innerHTML = totEmpA;
    document.getElementById('#education-p').innerHTML = entryEdA;
    document.getElementById('work-experience').innerHTML = workExpA;
    document.getElementById('job-wage-hourly-p').innerHTML = hMeanA;
    document.getElementById('job-wage-annual-p').innerHTML = aMeanA;
    document.getElementById('projected-growth-p').innerHTML = pctGrowA;
});