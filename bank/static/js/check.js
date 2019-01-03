function check_all() {
    var start_span = document.getElementById('start_time_span').innerText;
    var stop_span = document.getElementById('stop_time_span').innerText;
    if (start_span.length === 0 && stop_span.length === 0) {
        return true;
    }
    else {

        return false;
    }
}

function check_start_time() {
    var start_time = document.getElementById('start_time').value;
    $.get(
        '/project_management/check_start_time',
        {'c_time': start_time},
        function (data) {
            var span = document.getElementById('start_time_span');
            span.innerText = data.msg;
        },
        'json'
    )

}

function check_stop_time() {
    var stop_time = document.getElementById('stop_time').value;
    $.get(
        '/project_management/check_stop_time',
        {'c_time': stop_time},
        function (data) {
            var span = document.getElementById('stop_time_span');
            span.innerText = data.msg;
        },
        'json'
    )
}
