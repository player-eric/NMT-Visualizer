var layer_lookup_table = {};
function initialize_tree() {
  var config = {
    container: "#main_graph",
    rootOrientation: view_mode,
    hideRootNode: false,
    scrollbar: "native",
    node: {
      collapsable: true,
    },
    animation: {
      nodeAnimation: "easeOutBounce",
      nodeSpeed: 70,
      connectorsAnimation: "bounce",
      connectorsSpeed: 70,
    },
  };

  node_list = [];

  d3.json(json_dir, function (values) {
    total_translation = values.length;
    d3.select("#source_sentence").html(values[index]["source"]);
    d3.select("#target_sentence").html(values[index]["target"]);
    beam_width = values[index]["beam_width"];
    make_first_layer(values, node_list);
    total_layer = make_rest_layers(values, node_list);

    var chart = [config];

    for (i = 0; i < node_list.length; i++) {
      chart.push(node_list[i]);
    }

    tree = new Treant(chart);
    make_layer_lookup_table(tree, total_layer);
  });
}

function make_node(node_list, parent_id, word, has_children, prob, accum_prob) {
  var has = has_children == 1 ? "has" : "";
  if (is_whole == false) {
    var tmp = {
      parent: node_list[parent_id],
      text: { name: word, title: prob, desc: accum_prob },
      HTMLid: has,
      collapsed: true,
    };
  } else {
    var tmp = {
      parent: node_list[parent_id],
      text: { name: word, title: prob, desc: accum_prob },
      HTMLid: has,
    };
  }
  return tmp;
}

function make_first_layer(values, node_list) {
  history_ = values[index];

  var root = {
    text: { name: "<s>" },
    collapsed: true,
    HTMLid: "has",
  };
  node_list.push(root);

  var i = 0;
  for (j = 0; j < history_["predict"][i].length; j++) {
    node_list.push(
      make_node(
        node_list,
        0,
        history_["predict"][i][j],
        history_["has_children_lookup"][i][j],
        history_["probs"][i][j].toFixed(4),
        history_["accum_probs"][i][j].toFixed(4)
      )
    );
  }
}

function make_rest_layers(values, node_list) {
  history_ = values[index];
  for (i = 1; i < history_["predict"].length; i++) {
    for (j = 0; j < history_["predict"][j].length; j++) {
      parent_offset = history_["parent"][i][j];

      parent_id = beam_width * (i - 1) + parent_offset + 1;
      node_list.push(
        make_node(
          node_list,
          parent_id,
          history_["predict"][i][j],
          history_["has_children_lookup"][i][j],
          history_["probs"][i][j].toFixed(4),
          history_["accum_probs"][i][j].toFixed(4)
        )
      );
    }
  }

  return history_["predict"].length;
}

function expand_ith_node(i) {
  selected_node = tree.tree.nodeDB.db[i];

  selected_node.toggleCollapse();
}

function collapse_ith_node(i) {
  selected_node = tree.tree.nodeDB.db[i];
  selected_node.toggleCollapse();
}

function sleep(_ms = 0) {
  var _start = new Date().getTime();
  while (_ms > new Date().getTime() - _start) {}
}

function proceed() {
  if (current_layer > total_layer) {
    return;
  }

  layer_name = "layer_" + (current_layer - 1);
  to_expand = layer_lookup_table[layer_name][current_node];

  expand_ith_node(to_expand);

  if (current_layer == 1) {
    current_layer++;
  } else {
    current_node++;
    if (current_node >= layer_lookup_table[layer_name].length) {
      current_layer++;
      current_node = 0;
    }
  }
}

function expand_whole_tree() {
  is_whole = true;
  initialize_tree();
}

function make_layer_lookup_table(tree, total_layer) {
  var nodes = tree.tree.nodeDB.db;
  layer_lookup_table["layer_0"] = [0];
  for (i = 1; i < total_layer + 1; i++) {
    var prior_layer_name = "layer_" + (i - 1);
    var this_layer_name = "layer_" + i;

    tmp_node_list = [];
    for (j = 0; j < nodes.length; j++) {
      prior_layer_ids = layer_lookup_table[prior_layer_name];
      for (k = 0; k < prior_layer_ids.length; k++) {
        if (
          nodes[j].parentId == prior_layer_ids[k] &&
          nodes[j].children.length != 0
        ) {
          tmp_node_list.push(j);
          break;
        }
      }
    }
    layer_lookup_table[this_layer_name] = tmp_node_list;
  }
}
