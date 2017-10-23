import { Meteor } from 'meteor/meteor';
import { Mongo } from 'meteor/mongo';
// import '../imports/api/accounts.js';
import '../imports/api/methods.js';
// Postings = new Mongo.Collection('jobPostings');
// Meteor.publish('Posting',function(){
// 	return Postings.find({}, { sort: { Order: 1 } });
// });

// Meteor.methods({
  
//   'updatePostingOrder'( posts ) {
//   	console.log("Hellloooooo......");
//     check( posts, [{
//       _id: String,
//       Order: Number
//     }]);

//     for ( let post of posts ) {
//       posts.update( { _id: post._id }, { $set: { Order: post.Order } } );
//     }
//   }
// });