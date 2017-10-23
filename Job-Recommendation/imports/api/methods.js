// import { Meteor } from 'meteor/meteor';
// import { Mongo } from 'meteor/mongo';

import { Meteor } from 'meteor/meteor';
import { Mongo } from 'meteor/mongo';
import { check } from 'meteor/check';

Postings = new Mongo.Collection('jobPostings');
Meteor.publish('Posting',function(){
	return Postings.find({}, { sort: { Order: 1 } });
});
// ServerDummy = new Mongo.Collection('jobPostings');
// Meteor.publish('Postings',function(){
// 	return ServerDummy.find({}, { sort: { Order: 1 } });
// });
Meteor.methods({
  'updatePostingOrder'( posts ) {
  	console.log("Helloooooo............");
    check( posts, [{
      _id: String,
      Order: Number
    }]);

    for ( let post of posts ) {
      Postings.update( { _id: post._id }, { $set: { Order: post.Order } } );
    }
  }
});
