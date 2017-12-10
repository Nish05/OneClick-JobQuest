

import { Meteor } from 'meteor/meteor';
import { Mongo } from 'meteor/mongo';
import { check } from 'meteor/check';

Postings = new Mongo.Collection('cleanPostings_stem_test');
Meteor.publish('Posting',function(){
	return Postings.find({}, { sort: { Order: 1 } });
});

Resumes = new Mongo.Collection('cleanResume_stem_test');
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
      Postings.update( { "_id" : post._id}, {$set: { Order: post.Order } } );
    }
  }
});
