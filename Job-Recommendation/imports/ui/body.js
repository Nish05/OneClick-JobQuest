import { Template } from 'meteor/templating';
import { Account_Employees } from '../api/accounts.js';
import { Account_Seekers } from '../api/accounts.js';
import { Meteor } from 'meteor/meteor';
import './body.html';

ClientDummy = new Mongo.Collection('sampleCollection');

Template.Initial_login.events({
	'click .buttons' : function(event) {
		event.preventDefault();
	   	var action = event.target.value;
       	if(action == 'employee'){
       		Session.set({'user':'employee','option':true});
       	} else{
       	    Session.set({'user':'seeker','option':true});
       	}
	},
       
});

Template.Initial_login.helpers({
    "option" : function(){
    		return Session.get('option');
    },
    "user" : function(){
    		return Session.get('user');
    },
});
// Registration 
Template.register.events({
        'submit form': function(event) {
            event.preventDefault();
            var email = event.target.registerEmail.value;
        	  var password = event.target.registerPassword.value;
            console.log(password);
            // db.Account_Employees.insert({email:});
            Accounts.createUser({
    			    email: email,
            	password: password
			});
        },        
    });

// Login
Template.login.events({
        'submit form': function(event) {
            event.preventDefault();
            var emailVar = event.target.loginEmail.value;
        	  var passwordVar = event.target.loginPassword.value;
            // console.log("Form submitted.");
            Meteor.loginWithPassword(emailVar, passwordVar);
             if (Meteor.user()) {
               console.log(Meteor.userId());
            } else {
               console.log("ERROR: " + error.reason);
            }
        }
    });
// // Logout 
Template.dashboard.events({
    'click .logout': function(event){
        event.preventDefault();
         Meteor.logout(function(error) {

            if(error) {
               console.log("ERROR: " + error.reason);
            }
         });
    }
});
Template.hello.events({
	"click .showData" : function(){
			Session.set('button',true);
			// return temp;
	},
});
// Template.hello.onCreated(function helloOnCreated() {
//   this.counter = new ReactiveVar(0);
// });

Template.hello.helpers({
 
  "tempButton" : function(){
  			if(Session.get('button')){
				return Session.get('button');
  			}
  			
	},
});

Template.dataViewer.helpers({

	ClientDummy(){ 
		Meteor.subscribe('Postings');
	 	console.log(ClientDummy.find({}).fetch());	 
	 	return ClientDummy;
	 	
		
	},
	
});

