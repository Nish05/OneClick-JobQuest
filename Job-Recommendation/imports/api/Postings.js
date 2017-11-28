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
Resumes = new Mongo.Collection('resume');
Meteor.publish('Resume',function(){
	return Resumes.find({});
});

Meteor.methods({
  'updatePostingOrder'( posts ) {
    check( posts, [{
      _id: String,
      Order: Number
    }]);

    for ( let post of posts ) {
      // console.log("Post Info : id "+post._id+" Order : "+post.Order);
      // _id = post._id;
      Postings.update( { "_id" : post._id}, {$set: { Order: post.Order } } );
    }
  }
});
