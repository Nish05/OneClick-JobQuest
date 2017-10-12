import { Meteor } from 'meteor/meteor';
import { Mongo } from 'meteor/mongo';
// import '../imports/api/accounts.js';

ServerDummy = new Mongo.Collection('sampleCollection');
Meteor.publish('Postings',function(){
	return ServerDummy.find({});
});

