// http://stackoverflow.com/questions/12286332/twitter-bootstrap-remote-modal-shows-same-content-everytime

$(document).on('hidden.bs.modal', '.modal', function () {
  var modalData = $(this).data('bs.modal');
  
  // Destroy modal if has remote source 占쏙옙 don't want to destroy modals with static content.
  if (modalData && modalData.options.remote) {
    // Destroy component. Next time new component is created and loads fresh content
    $(this).removeData('bs.modal');
    // Also clear loaded content, otherwise it would flash before new one is loaded.
    $(this).find(".modal-content").empty();
  }

});