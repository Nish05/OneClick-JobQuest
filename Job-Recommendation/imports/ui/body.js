import { Template } from 'meteor/templating';
import { Meteor } from 'meteor/meteor';
import './body.html';
import { sortable } from 'html5sortable';

Postings = new Mongo.Collection('cleanPostings_stem_test');
Resumes = new Mongo.Collection('cleanResume_stem_test');

Template.Initial_login.events({
	'click .buttons' : function(event) {
		event.preventDefault();
	   	var action = event.target.value;
       	if(action == 'employee'){
       		Session.set({'user':'emp','option':true});
       	} else{
       	    Session.set({'user':'skr','option':true});
       	}
	},
       
});

Template.Initial_login.helpers({
    "option" : function(){
    		return Session.get('option');
    },
});
// Registration 
Template.register.events({
        'submit form': function(event) {
            event.preventDefault();
            var email = event.target.registerEmail.value;
        	  var password = event.target.registerPassword.value;
            console.log(password);
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


Template.hello.helpers({
 
  "tempButton" : function(){
				return Session.get('button');
	},
});
let initSortable = ( sortableClass ) => {
  let sortableList = $( sortableClass );
  sortableList.sortable( 'destroy' );
  sortableList.sortable();
  sortableList.sortable().off( 'sortupdate' );
  sortableList.sortable().on( 'sortupdate', () => {
    updateIndexes( '.sortable' );
  });
};
let updateIndexes = ( sortableClass ) => {
  let items = [];
  $( `${sortableClass} li` ).each( ( index, element ) => {
    items.push( { _id: $( element ).data( 'id' ), Order: (index + 1) } );
  });
  Meteor.call( 'updatePostingOrder', items, ( error ) => {
    if ( error ) {
      console.log( error.reason );
    }
  });
};
Template.dataViewer.onCreated( () => {
  let template = Template.instance();
  
    template.subscribe('Posting', () => {
          initSortable( '.sortable' );
    });
    template.subscribe('Resume', () => {
          initSortable( '.sortable' );
    });
});
Template.dataViewer.helpers({
    "user" : function(){
        return Session.get('user');
    },
    "resSeeker" : function() {
        if(Session.get('user') == 'emp'){
          return Resumes.find();
       } 
    },
    "resEmp" : function(){
       if(Session.get('user') == 'skr'){
          return Postings.find();
       } 
     },
     
});



