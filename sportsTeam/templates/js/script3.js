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
var annArray = [];
var ann_10 = 0;
var ann_25 = 0;
var ann_m = 0;
var ann_75 = 0;
var ann_90 = 0;


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
    //console.log(data)
    
    dataObj = $.parseJSON(data);
        
        for (var i=0; i < dataObj.length; i++){
            jobTitle.push(dataObj[i].OCC_TITLE);
            pctGrow.push(dataObj[i].PCT_GROWTH);
            workExp.push(dataObj[i].WORK_EXP);
            totEmp.push(dataObj[i].TOT_EMP);
            entryEd.push(dataObj[i].ENTRY_ED);
            aMean.push(dataObj[i].A_MEAN);
            hMean.push(dataObj[i].H_MEAN);
            
            tempA_PCT10 = dataObj[i].A_PCT10;
            A_PCT10.push(Number(tempA_PCT10.replace(/[^0-9\.]+/g,"")));
            
            tempA_PCT25 = dataObj[i].A_PCT25;
            A_PCT25.push(Number(tempA_PCT25.replace(/[^0-9\.]+/g,"")));
            
            tempA_MD = dataObj[i].A_MEDIAN;
            A_MD.push(Number(tempA_MD.replace(/[^0-9\.]+/g,"")));
            
            tempA_PCT75 = dataObj[i].A_PCT75;
            A_PCT75.push(Number(tempA_PCT75.replace(/[^0-9\.]+/g,"")));
            
            tempA_PCT90 = dataObj[i].A_PCT90;
            A_PCT90.push(Number(tempA_PCT90.replace(/[^0-9\.]+/g,"")));
        }; 

    console.log(A_PCT25);
    generateDropDown();
    generateData();
};

function generateDropDown(){
    for (var i in jobTitle){
        $("#selectbox").append('<option value="'+jobTitle[i]+' selected="selected"">'+jobTitle[i]+'</option>');
    };
};

function generateData(){
    var e = document.getElementById("selectbox");
    var active = e.options[e.selectedIndex].text;

    console.log(active);
};

function run() {
    var dropdown = document.getElementById("selectbox");
    var i = dropdown.options[dropdown.selectedIndex].index;
    var title = "";
    var total = "";
    var education = "";
    var experience = "";
    var hourly = "";
    var annual = "";
    var percent = "";
 
    

    //console.log(i)
    
    if (jobTitle[i]){
        title += jobTitle[i];
        total += totEmp[i];
        education += entryEd[i];
        experience += workExp[i];
        hourly += "$" + hMean[i];
        annual += "$" + aMean[i];
        percent+= "+" + pctGrow[i] + "%";
        ann_10 += A_PCT10[i];
        ann_25 += A_PCT25[i];
        ann_m += A_MD[i];
        ann_75 += A_PCT75[i];
        ann_90 += A_PCT90[i];
        };
        //console.log(title);
        document.getElementById("job-title-p").innerHTML = title;
        document.getElementById("total-p").innerHTML = total;
        document.getElementById("education-p").innerHTML = education;
        document.getElementById("work-experience-p").innerHTML = experience;
        document.getElementById("job-wage-hourly-p").innerHTML = hourly;
        document.getElementById("job-wage-annual-p").innerHTML = annual;
        document.getElementById("projected-growth-p").innerHTML = percent;
        //console.log(ann_10)
        
        var annArray = [ann_10, ann_25, ann_m, ann_75, ann_90];
        
        console.log(annArray)
    

        generateChart();

        };


function generateChart(){
    $('#annual-chart').highcharts({    
        title: {
            text: 'Annual Salary'
        },
        subtitle: {
            text: 'based on percentiles'
        },
        xAxis: {
            categories: ["10th Percentile", "25th Percentile", "Median", "75th Percentile", "90th Percentile"]
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Annual Salary (US Dollars)'
            },
             plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                '<td style="padding:0"><b>${point.y:.2f} </b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        colors: ['#1e6388'],
        credits: {
            enabled: false
        },
        legend: {
            enabled: false
        },
        plotOptions: {
            column: {
                pointPadding: 0.2,
                borderWidth: 0
            }
        },
        series: [{
            name: "salary",
            data: [ann_10, ann_25, ann_m, ann_75, ann_90]
            }]
    });
};
    


