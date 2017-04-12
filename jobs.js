var app = angular.module("JobsApp", ['ngRoute'])

app.config(function ($routeProvider) {
    $routeProvider
        .when("/apply", { //application view with applicaiton form
            templateUrl: "application.html"
        })
        .when("/main", { //main view with list of vacancies
            templateUrl: "vacancies.html"
        })
        .otherwise({    //any other url returns main
            redirectTo: "/main"
        });
});



app.controller("myCtrl", myJsCtrl);

function myJsCtrl($http, $window, $location) { 
    var self = this;
    self.myArray = [];//array of vacancies
    $http.get("http://localhost:5050",  //get request to fetch all vacancies
        { dataType: "json" })
        .success(function (response) {  //get request is successfull, 
            self.myArray = response.jobs;//jobs are listed
        })
    self.apply = function (index) { //application view is enabled
        $location.path('/apply');
        self.selected = index;  //the ID of the selected vacancy
    }
    self.submit = function () {
        //put request to apply
        $http.put("http://localhost:5050/" + self.myArray[self.selected].id)
            .success(function (response) {  //successful put request
                self.myArray[self.selected].applied = 1;
                alert("Application made for job"+self.myArray[self.selected].name);//pop up message
            })
        
    }
    self.cancel = function () {
        $location.path('/main'); //back to main page
    }
}
