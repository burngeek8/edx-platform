define(["backbone", "underscore"], function(Backbone, _) {
// this file should be refactored so that it returns a single object, rather than
// attaching several models to the `window` object.
window.CMS = window.CMS || {};
CMS.Models = CMS.Models || {};

CMS.Models.CourseRelative = Backbone.Model.extend({
	defaults: {
		course_location : null, // must never be null, but here to doc the field
		idx : null	// the index making it unique in the containing collection (no implied sort)
	}
});

CMS.Models.CourseRelativeCollection = Backbone.Collection.extend({
	model : CMS.Models.CourseRelative
});

}); // end define()
