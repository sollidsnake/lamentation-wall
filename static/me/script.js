function cryTogether(id, waitMessage, okMessage, failMessage) {
    scroll = $(document).scrollTop();
    //$('#lamentations').css('height', $('#lamentations').height() + 'px');
    startLoading();

    //$('#lamentations').html(waitMessage);

    $.ajax({
	    url: "/crytogether",
	    data: { 'id': id },
	    context: document.body
    }).done(function(data) {
	    $('#lamentations').load(location.href + ' #lamentatios-reload',
				                function() {
                                    //$('#lamentations').css('height', 'auto');
				                    //$(document).scrollTop(scroll);
                                    stopLoading();
				                });
    }).fail(function(data) {
	    alert(failMessage);
        stopLoading();
    });
}

function uncry(lamentId, waitMessage, okMessage, failMessage) {
    startLoading();

    $.ajax({
	    url: "/uncry",
	    data: { 'id': lamentId },
	    context: document.body
    }).done(function(data) {
	    $('#lamentations').load(location.href + ' #lamentatios-reload',
				                function() {
                                    //$('#lamentations').css('height', 'auto');
				                    //$(document).scrollTop(scroll);
                                    stopLoading();
				                });
    }).fail(function(data) {
	    alert(failMessage);
        stopLoading();
    });
    
}

function startLoading(context) {
    $('#loading-indicator').fadeIn(200);
}

stopLoading();
function stopLoading() {
    $('#loading-indicator').fadeOut(200);
    //$('body').removeClass('loading-indicator-body');
}

function giveCounselModal(id) {
    $('#id_counsel-lament_id').val(id);

    $('#navheader').css('width', $('#navheader').css('width'));
    loadCounsels(true);
}

$('#counsel-modal').on('shown.bs.modal', function () {
    autoFocus('#id_counsel-text', false);
    $('#navheader').css('width', navheaderWidth);
})

$('#counsel-modal').on('hidden.bs.modal', function () {
    $('#navheader').css('width', 'auto');
})

function autoFocus(el, ignoreMobile) {
    if(typeof ignoreMobile === 'undefined')  ignoreMobile = true;
    focus = false;
    if(!$.browser.mobile) {
        focus = true;
    } else if($.browser.mobile && ignoreMobile==false) {
        focus = true;
    }

    if(focus) $(el).focus();
}

function loadCounsels(loading) {
    if(loading==true)
	startLoading();
    $('#counsel-list').
        load('list-counsels?lament=' +
             $('#id_counsel-lament_id').val(),
             function() {
                 $('#counsel-modal').modal('show');

                 $('#id_counsel-text').val('');

		 if(loading==true)
                     stopLoading();

		 if(jQuery.trim($('#counsel-list').html()).length == 0) {
		     $('#counsel-list').css('display', 'none');
		 } else
		     $('#counsel-list').css('display', 'block');
             });
}

var navheaderWidth;

$(document).ready(function() {
    autoFocus('#id_lamentation-text');


    $('#counsel-form').submit(function() {
	startLoading();
        if($('#counsel-form').parsley().validate()) {
            $.ajax({
                method: 'POST',
                url: '/save-counsel',
                data: $(this).serialize(),
                type: 'POST',

                success: function(response) {
                    //$('#counsel-modal').modal('hide');
                    data = JSON.parse(response);
                    loadCounsels(false);
                    $('#id_counsel-text').val('');

                    $('#counsels_count_'+data.lament_id).html(data.count);

		    stopLoading();
                }

            });
        }

        return false;
    });

    window.dispatchEvent(new Event('resize'));
});

if($.browser.mobile && $.browser.mozilla) {
    $('#lamentations').css('height', 'auto');
    $('#lament-header').removeClass('navbar-fixed-top');
    //$('body').removeClass('body');
}

$(function () {
    //$('[data-toggle="popover"]').popover();

    $('#lament-form').submit(function() {
        if (grecaptcha.getResponse() == "") {
            return false;
        }

        return true;
    });

    $('[data-toggle="popover"]').popover({
        container: '#lamentations'
    });
});
$('body').on('click', function (e) {
    //only buttons
    if ($(e.target).data('toggle') !== 'popover'
        && $(e.target).parents('.popover.in').length === 0) { 
        $('[data-toggle="popover"]').popover('hide');
    }
    //buttons and icons within buttons
    /*
    if ($(e.target).data('toggle') !== 'popover'
        && $(e.target).parents('[data-toggle="popover"]').length === 0
        && $(e.target).parents('.popover.in').length === 0) { 
        $('[data-toggle="popover"]').popover('hide');
    }
    */
});
