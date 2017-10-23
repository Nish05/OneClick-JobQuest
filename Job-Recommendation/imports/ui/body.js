import { Template } from 'meteor/templating';
import { Account_Employees } from '../api/accounts.js';
import { Account_Seekers } from '../api/accounts.js';
import { Meteor } from 'meteor/meteor';
import './body.html';
import { sortable } from 'html5sortable';
// import { check } from 'meteor/check';

Postings = new Mongo.Collection('jobPostings');

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
            Meteor.loginWithPassword(emailVar, passwordVar, function(error){
            if (error) {
               console.log("ERROR: "+ error.reason);
            } else {
               console.log(Meteor.userId());
            }

            });
            
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
let initSortable = ( sortableClass ) => {
  let sortableList = $( sortableClass );
  // console.log("Sortable list : "+ sortableList);
  sortableList.sortable( 'destroy' );
  sortableList.sortable();
  sortableList.sortable().off( 'sortupdate' );
  sortableList.sortable().on( 'sortupdate', () => {
    // console.log("On line 102");
    updateIndexes( '.sortable' );
  });
};
let updateIndexes = ( sortableClass ) => {
  let items = [];
  // console.log("Hellllllooooooooo.......");
  $( `${sortableClass} li` ).each( ( index, element ) => {
    // console.log("Id : "+$( element ).data( 'id' )+"Order : "+ (index+1));
    items.push( { _id: $( element ).data( 'id' ), Order: (index + 1) } );
  });
  Meteor.call( 'updatePostingOrder', items, ( error ) => {
    if ( error ) {
      console.log( error.reason );
    }
  });
};

// Template.dataViewer.helpers({

// 	ClientDummy(){ 
// 		Meteor.subscribe('Postings', () => {
//           console.log("Line number 124 .........");
//           // initSortable( '.sortable' );
//     });
// 	 	// console.log(ClientDummy.find({}).fetch());	 
// 	 	// return ClientDummy.find({}).fetch();z
// 	},
	
// });
Template.dataViewer.onCreated( () => {
  let template = Template.instance();
  
    template.subscribe('Posting', () => {
          initSortable( '.sortable' );
    });
});
Template.dataViewer.helpers({
    "jobs" : function(){
      return Postings.find();
    },
});
// Meteor.methods({
  
//   'updatePostingOrder'( posts ) {
//    console.log("Hellloooooo......");
//     check( posts, [{
//       _id: String,
//       Order: Number
//     }]);

//     for ( let post of posts ) {
//       posts.update( { _id: post._id }, { $set: { Order: post.Order } } );
//     }
//   }
// });


