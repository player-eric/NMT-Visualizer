function change_view_mode(mode) {
  if (mode == "horizontal") {
    view_mode = "WEST";
  } else {
    view_mode = "NORTH";
  }
  initialize_tree(view_mode);
}

function change_expand_mode(mode) {
  if (mode == "step") {
    d3.select("#expand_all")
      .attr(
        "style",
        "position: absolute;top: 1%;left: 70%;background-color: grey;color: white;text-decoration: none;display: inline-block;padding: 8px 16px;"
      )
      .attr("href", null);
    d3.select("#step")
      .attr(
        "style",
        "position: absolute;top: 1%;left: 63%;background-color: #20d2a6;color: white;text-decoration: none;display: inline-block;padding: 8px 16px;"
      )
      .attr("href", "#");
    is_whole = false;
  } else {
    d3.select("#expand_all")
      .attr(
        "style",
        "position: absolute;top: 1%;left: 70%;background-color: #20d2a6;color: white;text-decoration: none;display: inline-block;padding: 8px 16px;"
      )
      .attr("href", "#");
    d3.select("#step")
      .attr(
        "style",
        "position: absolute;top: 1%;left: 63%;background-color: grey;color: white;text-decoration: none;display: inline-block;padding: 8px 16px;"
      )
      .attr("href", null);
    is_whole = true;
  }
  initialize_tree();
}

function increase_index() {
  index += 1;
  if (index > total_translation - 1) {
    index = 0;
  }
  d3.select("#index").html(index);
  current_layer = 1;
  current_node = 0;
  initialize_tree();
}

function decrease_index() {
  index -= 1;
  if (index < 0) {
    index = total_translation - 1;
  }
  d3.select("#index").html(index);
  current_layer = 1;
  current_node = 0;
  initialize_tree();
}

function save() {
  domtoimage.toSvg(document.getElementById("main_graph")).then(function (blob) {
    window.saveAs(blob, "beam_search_decode.svg");
  });
}

function expand_all() {
  expand_ith_node(0);
}

function reset() {
  is_whole = false;
  current_layer = 1;
  current_node = 0;
  initialize_tree();
}

function resize() {
  var example_x, example_y, example_w, example_h;
  var w = window.innerWidth;
  var h = window.innerHeight;
  example_x = w * 0.01;
  example_y = h * 0.84;
  example_w = w * 0.16;
  example_h = h * 0.15;

  d3.select("#example").attr(
    "style",
    "position: absolute;top: " +
      example_y +
      "px;left: " +
      example_x +
      "px;width: " +
      example_w +
      "px;height: " +
      example_h +
      "px;"
  );
}
