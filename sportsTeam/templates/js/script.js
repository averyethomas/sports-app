var data;
var jobTitle = [];
var A_PCT10 = [];
var A_PCT25 = [];
var A_MD = [];
var A_PCT75 = [];
var A_PCT90 = [];
var totEmp = [];
var entryEd = [];
var workExp = [];
var pctGrow = [];
var aMean = [];
var hMean = [];
//not what I wanted to do originally but wanted to show layout
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
    loadData();
});

function loadData(){
    $.ajax({
            type:"GET",
            url:"js/data.json",
            dataType:"text",
            success: parseData
    });
};


function parseData(data){
    console.log(data)
    
    dataObj = $.parseJSON(data);
        
        for (var i=0; i < dataObj.length; i++){
            jobTitle.push(dataObj[i].OCC_TITLE);
            pctGrow.push(dataObj[i].PCT_GROWTH);
            workExp.push(dataObj[i].WORK_EXP);
            A_PCT10.push(dataObj[i].A_PCT10);
            A_PCT25.push(dataObj[i].A_PCT25);
            A_MD.push(dataObj[i].A_MEDIAN);
            A_PCT75.push(dataObj[i].A_PCT75);
            A_PCT90.push(dataObj[i].A_PCT90);
            totEmp.push(dataObj[i].TOT_EMP);
            entryEd.push(dataObj[i].ENTRY_ED);
            aMean.push(dataObj[i].A_MEAN);
            hMean.push(dataObj[i].H_MEAN);
        }; 

    console.log(jobTitle);
    document.getElementById('#job-title-p').innerHTML = jobTitleA;
    document.getElementById('#total-p').innerHTML = totEmpA;
    document.getElementById('#education-p').innerHTML = entryEdA;
    document.getElementById('work-experience').innerHTML = workExpA;
    document.getElementById('job-wage-hourly-p').innerHTML = hMeanA;
    document.getElementById('job-wage-annual-p').innerHTML = aMeanA;
    document.getElementById('projected-growth-p').innerHTML = pctGrowA;
    generateDropDown();
    generateChart();
    //generateData();
};

function generateDropDown(){
    for (var i in jobTitle){
        $("#selectbox").append('<option value="'+jobTitle[i]+'">'+jobTitle[i]+'</option>');
    };
};

function generateChart(){
    $('#annual-chart').highcharts({
        chart: {
            type: 'column'
        },
        title: {
            text: 'Annual Salary'
        },
        subtitle: {
            text: 'based on percentile'
        },
        xAxis: {
            categories: ["10th", "25th", "Median", "75th", "90th"] 
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Salary (US Dollars)'
            }
        },
        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                '<td style="padding:0"><b>${point.y:.2f} </b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        plotOptions: {
            column: {
                pointPadding: 0.2,
                borderWidth: 0
            }
        },
        series: [{
            name: 'Architecture',
            data: [A_PCT10_A, A_PCT25_A, A_MD_A, A_PCT75_A, A_PCT90_A],
            }]
        })


//Goal was to do something along these lines to make it popuate based on selection in drop down-
//function generateData(){
    //if (jobTitle=[i]){
        //document.getElementById('#job-title-p').innerHTML = jobTitle[i];
        //document.getElementById('#job-category-p').innerHTML = jobCatBig[i];
        //document.getElementById('#total-p').innerHTML = totEmp[i];
        //document.getElementById('#education-p').innerHTML = entryEd[i];
        //document.getElementById('work-experience').innerHTML = workExp[i];
        //document.getElementById('job-wage-hourly-p').innerHTML = hMean[i];
        //document.getElementById('job-wage-annual-p').innerHTML = aMean[i];
        //document.getElementById('projected-growth-p').innerHTML = pctGrow[i];
   // };
//};


