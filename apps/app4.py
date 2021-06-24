import dash
import dash_dangerously_set_inner_html
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
#import dash_table_experiments as dt
from functools import lru_cache
import datetime

from app import app, cache

from dash.dependencies import Input, Output
import plotly.express as px


def layout4():
    return html.Div([
        dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
        <!-- some code adapted from www.degeneratestate.org/static/metal_lyrics/metal_line.html -->
<!-- <!DOCTYPE html>
<meta content="utf-8"> -->
<style>
    /* set the CSS */
    body {
        font: 12px Arial;
    }

    svg {
        font: 12px Helvetica;
    }

    path {
        stroke: steelblue;
        stroke-width: 2;
        fill: none;
    }

    .grid line {
        stroke: lightgrey;
        stroke-opacity: 0.4;
        shape-rendering: crispEdges;
    }

    .grid path {
        stroke-width: 0;
    }

    .axis path,
    .axis lineper {
        fill: none;
        stroke: grey;
        stroke-width: 1;
        shape-rendering: crispEdges;
    }

    div.tooltip {
        position: absolute;
        text-align: center;
        width: 150px;
        height: 28px;
        padding: 2px;
        font: 12px sans-serif;
        background: lightsteelblue;
        border: 0px;
        border-radius: 8px;
        pointer-events: none;
    }

    div.tooltipscore {
        position: absolute;
        text-align: center;
        width: 150px;
        height: 50px;
        padding: 2px;
        font: 10px sans-serif;
        background: lightsteelblue;
        border: 0px;
        border-radius: 8px;
        pointer-events: none;
    }

    .category_header {
        font: 12px sans-serif;
        font-weight: bolder;
        text-decoration: underline;
    }

    div.label {
        color: rgb(252, 251, 253);
        color: rgb(63, 0, 125);
        color: rgb(158, 155, 201);
        position: absolute;
        text-align: left;
        padding: 1px;
        border-spacing: 1px;
        font: 10px sans-serif;
        font-family: Sans-Serif;
        border: 0;
        pointer-events: none;
    }

    /*
input {
  border: 1px dotted #ccc;
  background: white;
  font-family: monospace;
  padding: 10px 20px;
  font-size: 14px;
  margin: 20px 10px 30px 0;
  color: darkred;
}*/
    .alert {
        font-family: monospace;
        padding: 10px 20px;
        font-size: 14px;
        margin: 20px 10px 30px 0;
        color: darkred;
    }

    ul.top_terms li {
        padding-right: 20px;
        font-size: 30pt;
        color: red;
    }

    /*
input:focus {
  background-color: lightyellow;
  outline: none;
}*/
    .snippet {
        padding-bottom: 10px;
        padding-left: 5px;
        padding-right: 5px;
        white-space: pre-wrap;
    }

    .snippet_header {
        font-size: 20px;
        font-family: Helvetica, Arial, Sans-Serif;
        font-weight: bolder;
        text-decoration: underline;
        text-align: center;
        border-bottom-width: 10px;
        border-bottom-color: #888888;
        padding-bottom: 10px;
    }

    .topic_preview {
        font-size: 12px;
        font-family: Helvetica, Arial, Sans-Serif;
        text-align: center;
        padding-bottom: 10px;
        font-weight: normal;
        text-decoration: none;
    }

    #d3-div-1-categoryinfo {
        font-size: 12px;
        font-family: Helvetica, Arial, Sans-Serif;
        text-align: center;
        padding-bottom: 10px;
    }

    #d3-div-1-title-div {
        font-size: 20px;
        font-family: Helvetica, Arial, Sans-Serif;
        text-align: center;
    }

    .text_header {
        font: 18px sans-serif;
        font-size: 18px;
        font-family: Helvetica, Arial, Sans-Serif;
        font-weight: bolder;
        text-decoration: underline;
        text-align: center;
        color: darkblue;
        padding-bottom: 10px;
    }

    .text_subheader {
        font-size: 14px;
        font-family: Helvetica, Arial, Sans-Serif;
        text-align: center;
    }

    .snippet_meta {
        border-top: 3px solid #4588ba;
        font-size: 12px;
        font-family: Helvetica, Arial, Sans-Serif;
        color: darkblue;
    }

    .not_match {
        background-color: #f0f8ff;
    }

    .contexts {
        width: 45%;
        float: left;
    }

    .neut_display {
        display: none;
        float: left;
    }

    .scattertext {
        font-size: 10px;
        font-family: Helvetica, Arial, Sans-Serif;
    }

    .label {
        font-size: 10px;
        font-family: Helvetica, Arial, Sans-Serif;
    }

    .obscured {
        /*font-size: 14px;
  font-weight: normal;
  color: dimgrey;
  font-family: Helvetica;*/
        text-align: center;
    }

    .small_label {
        font-size: 10px;
    }

    #d3-div-1-corpus-stats {
        text-align: center;
    }

    #d3-div-1-cat {}

    #d3-div-1-notcat {}

    #d3-div-1-neut {}

    #d3-div-1-neutcol {
        display: none;
    }

    /* Adapted from https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_autocomplete */
    .autocomplete {
        position: relative;
        display: inline-block;
    }

    input {
        border: 1px solid transparent;
        background-color: #f1f1f1;
        padding: 10px;
        font-size: 16px;
    }

    input[type="text"] {
        background-color: #f1f1f1;
        width: 100%;
    }

    input[type="submit"] {
        background-color: DodgerBlue;
        color: #fff;
        cursor: pointer;
    }

    .autocomplete-items {
        position: absolute;
        border: 2px solid #d4d4d4;
        border-bottom: none;
        border-top: none;
        z-index: 99;
        /*position the autocomplete items to be the same width as the container:*/
        top: 100%;
        left: 0;
        right: 0;
    }

    .autocomplete-items div {
        padding: 10px;
        cursor: pointer;
        background-color: #fff;
        border-bottom: 2px solid #d4d4d4;
    }

    /*when hovering an item:*/
    .autocomplete-items div:hover {
        background-color: #e9e9e9;
    }

    /*when navigating through the items using the arrow keys:*/
    .autocomplete-active {
        background-color: DodgerBlue !important;
        color: #ffffff;
    }
</style>
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/4.6.0/d3.min.js" charset="utf-8"></script>
<script src="https://d3js.org/d3-scale-chromatic.v1.min.js" charset="utf-8"></script>
<!-- INSERT SEMIOTIC SQUARE -->
<!--<a onclick="maxFreq = Math.log(data.map(d => d.cat + d.ncat).reduce((a,b) => Math.max(a,b))); plotInterface.redrawPoints(0.1, d => (Math.log(d.ncat + d.cat)/maxFreq), d => d.s, false); plotInterface.redrawPoints(0.1, d => (Math.log(d.ncat + d.cat)/maxFreq), d => d.s, true)">View Score Plot</a>-->
<span id="d3-div-1-title-div"></span>
<div class="scattertext" id="d3-div-1" style="float: left"></div>
<div style="floag: left">
    <div autocomplete="off">
        <div class="autocomplete">
            <input id="searchInput" type="text" placeholder="Search the chart" />
        </div>
    </div>
</div>
<br />
<div id="d3-div-1-corpus-stats"></div>
<div id="d3-div-1-overlapped-terms"></div>
<a name="d3-div-1-snippets"></a>
<a name="d3-div-1-snippetsalt"></a>
<div id="d3-div-1-termstats"></div>
<div id="d3-div-1-overlapped-terms-clicked"></div>
<div id="d3-div-1-categoryinfo" style="display: hidden"></div>
<div id="d3-div-2">
    <div class="d3-div-1-contexts">
        <div class="snippet_header" id="d3-div-1-cathead"></div>
        <div class="snippet" id="d3-div-1-cat"></div>
    </div>
    <div id="d3-div-1-notcol" class="d3-div-1-contexts">
        <div class="snippet_header" id="d3-div-1-notcathead"></div>
        <div class="snippet" id="d3-div-1-notcat"></div>
    </div>
    <div id="d3-div-1-neutcol" class="d3-div-1-contexts">
        <div class="snippet_header" id="d3-div-1-neuthead"></div>
        <div class="snippet" id="d3-div-1-neut"></div>
    </div>
</div>
<script charset="utf-8">
    // Created using Cozy: github.com/uwplse/cozy
    function Rectangle(ax1, ay1, ax2, ay2) {
        this.ax1 = ax1;
        this.ay1 = ay1;
        this.ax2 = ax2;
        this.ay2 = ay2;
        this._left7 = undefined;
        this._right8 = undefined;
        this._parent9 = undefined;
        this._min_ax12 = undefined;
        this._min_ay13 = undefined;
        this._max_ay24 = undefined;
        this._height10 = undefined;
    }

    function RectangleHolder() {
        this.my_size = 0;
        this._root1 = null;
    }
    RectangleHolder.prototype.size = function () {
        return this.my_size;
    };
    RectangleHolder.prototype.add = function (x) {
        ++this.my_size;
        var _idx69 = x.ax2;
        x._left7 = null;
        x._right8 = null;
        x._min_ax12 = x.ax1;
        x._min_ay13 = x.ay1;
        x._max_ay24 = x.ay2;
        x._height10 = 0;
        var _previous70 = null;
        var _current71 = this._root1;
        var _is_left72 = false;
        while (!(_current71 == null)) {
            _previous70 = _current71;
            if (_idx69 < _current71.ax2) {
                _current71 = _current71._left7;
                _is_left72 = true;
            } else {
                _current71 = _current71._right8;
                _is_left72 = false;
            }
        }
        if (_previous70 == null) {
            this._root1 = x;
        } else {
            x._parent9 = _previous70;
            if (_is_left72) {
                _previous70._left7 = x;
            } else {
                _previous70._right8 = x;
            }
        }
        var _cursor73 = x._parent9;
        var _changed74 = true;
        while (_changed74 && !(_cursor73 == null)) {
            var _old__min_ax1275 = _cursor73._min_ax12;
            var _old__min_ay1376 = _cursor73._min_ay13;
            var _old__max_ay2477 = _cursor73._max_ay24;
            var _old_height78 = _cursor73._height10;
            /* _min_ax12 is min of ax1 */
            var _augval79 = _cursor73.ax1;
            var _child80 = _cursor73._left7;
            if (!(_child80 == null)) {
                var _val81 = _child80._min_ax12;
                _augval79 = _augval79 < _val81 ? _augval79 : _val81;
            }
            var _child82 = _cursor73._right8;
            if (!(_child82 == null)) {
                var _val83 = _child82._min_ax12;
                _augval79 = _augval79 < _val83 ? _augval79 : _val83;
            }
            _cursor73._min_ax12 = _augval79;
            /* _min_ay13 is min of ay1 */
            var _augval84 = _cursor73.ay1;
            var _child85 = _cursor73._left7;
            if (!(_child85 == null)) {
                var _val86 = _child85._min_ay13;
                _augval84 = _augval84 < _val86 ? _augval84 : _val86;
            }
            var _child87 = _cursor73._right8;
            if (!(_child87 == null)) {
                var _val88 = _child87._min_ay13;
                _augval84 = _augval84 < _val88 ? _augval84 : _val88;
            }
            _cursor73._min_ay13 = _augval84;
            /* _max_ay24 is max of ay2 */
            var _augval89 = _cursor73.ay2;
            var _child90 = _cursor73._left7;
            if (!(_child90 == null)) {
                var _val91 = _child90._max_ay24;
                _augval89 = _augval89 < _val91 ? _val91 : _augval89;
            }
            var _child92 = _cursor73._right8;
            if (!(_child92 == null)) {
                var _val93 = _child92._max_ay24;
                _augval89 = _augval89 < _val93 ? _val93 : _augval89;
            }
            _cursor73._max_ay24 = _augval89;
            _cursor73._height10 = 1 + ((_cursor73._left7 == null ? -1 : _cursor73._left7._height10) > (_cursor73
                    ._right8 == null ? -1 : _cursor73._right8._height10) ? _cursor73._left7 == null ? -1 :
                _cursor73._left7._height10 : _cursor73._right8 == null ? -1 : _cursor73._right8._height10);
            _changed74 = false;
            _changed74 = _changed74 || !(_old__min_ax1275 == _cursor73._min_ax12);
            _changed74 = _changed74 || !(_old__min_ay1376 == _cursor73._min_ay13);
            _changed74 = _changed74 || !(_old__max_ay2477 == _cursor73._max_ay24);
            _changed74 = _changed74 || !(_old_height78 == _cursor73._height10);
            _cursor73 = _cursor73._parent9;
        }
        /* rebalance AVL tree */
        var _cursor94 = x;
        var _imbalance95;
        while (!(_cursor94._parent9 == null)) {
            _cursor94 = _cursor94._parent9;
            _cursor94._height10 = 1 + ((_cursor94._left7 == null ? -1 : _cursor94._left7._height10) > (_cursor94
                    ._right8 == null ? -1 : _cursor94._right8._height10) ? _cursor94._left7 == null ? -1 :
                _cursor94._left7._height10 : _cursor94._right8 == null ? -1 : _cursor94._right8._height10);
            _imbalance95 = (_cursor94._left7 == null ? -1 : _cursor94._left7._height10) - (_cursor94._right8 ==
                null ? -1 : _cursor94._right8._height10);
            if (_imbalance95 > 1) {
                if (
                    (_cursor94._left7._left7 == null ? -1 : _cursor94._left7._left7._height10) < (_cursor94._left7
                        ._right8 == null ? -1 : _cursor94._left7._right8._height10)) {
                    /* rotate ((_cursor94)._left7)._right8 */
                    var _a96 = _cursor94._left7;
                    var _b97 = _a96._right8;
                    var _c98 = _b97._left7;
                    /* replace _a96 with _b97 in (_a96)._parent9 */
                    if (!(_a96._parent9 == null)) {
                        if (_a96._parent9._left7 == _a96) {
                            _a96._parent9._left7 = _b97;
                        } else {
                            _a96._parent9._right8 = _b97;
                        }
                    }
                    if (!(_b97 == null)) {
                        _b97._parent9 = _a96._parent9;
                    }
                    /* replace _c98 with _a96 in _b97 */
                    _b97._left7 = _a96;
                    if (!(_a96 == null)) {
                        _a96._parent9 = _b97;
                    }
                    /* replace _b97 with _c98 in _a96 */
                    _a96._right8 = _c98;
                    if (!(_c98 == null)) {
                        _c98._parent9 = _a96;
                    }
                    /* _min_ax12 is min of ax1 */
                    var _augval99 = _a96.ax1;
                    var _child100 = _a96._left7;
                    if (!(_child100 == null)) {
                        var _val101 = _child100._min_ax12;
                        _augval99 = _augval99 < _val101 ? _augval99 : _val101;
                    }
                    var _child102 = _a96._right8;
                    if (!(_child102 == null)) {
                        var _val103 = _child102._min_ax12;
                        _augval99 = _augval99 < _val103 ? _augval99 : _val103;
                    }
                    _a96._min_ax12 = _augval99;
                    /* _min_ay13 is min of ay1 */
                    var _augval104 = _a96.ay1;
                    var _child105 = _a96._left7;
                    if (!(_child105 == null)) {
                        var _val106 = _child105._min_ay13;
                        _augval104 = _augval104 < _val106 ? _augval104 : _val106;
                    }
                    var _child107 = _a96._right8;
                    if (!(_child107 == null)) {
                        var _val108 = _child107._min_ay13;
                        _augval104 = _augval104 < _val108 ? _augval104 : _val108;
                    }
                    _a96._min_ay13 = _augval104;
                    /* _max_ay24 is max of ay2 */
                    var _augval109 = _a96.ay2;
                    var _child110 = _a96._left7;
                    if (!(_child110 == null)) {
                        var _val111 = _child110._max_ay24;
                        _augval109 = _augval109 < _val111 ? _val111 : _augval109;
                    }
                    var _child112 = _a96._right8;
                    if (!(_child112 == null)) {
                        var _val113 = _child112._max_ay24;
                        _augval109 = _augval109 < _val113 ? _val113 : _augval109;
                    }
                    _a96._max_ay24 = _augval109;
                    _a96._height10 = 1 + ((_a96._left7 == null ? -1 : _a96._left7._height10) > (_a96._right8 ==
                            null ? -1 : _a96._right8._height10) ? _a96._left7 == null ? -1 : _a96._left7
                        ._height10 : _a96._right8 == null ? -1 : _a96._right8._height10);
                    /* _min_ax12 is min of ax1 */
                    var _augval114 = _b97.ax1;
                    var _child115 = _b97._left7;
                    if (!(_child115 == null)) {
                        var _val116 = _child115._min_ax12;
                        _augval114 = _augval114 < _val116 ? _augval114 : _val116;
                    }
                    var _child117 = _b97._right8;
                    if (!(_child117 == null)) {
                        var _val118 = _child117._min_ax12;
                        _augval114 = _augval114 < _val118 ? _augval114 : _val118;
                    }
                    _b97._min_ax12 = _augval114;
                    /* _min_ay13 is min of ay1 */
                    var _augval119 = _b97.ay1;
                    var _child120 = _b97._left7;
                    if (!(_child120 == null)) {
                        var _val121 = _child120._min_ay13;
                        _augval119 = _augval119 < _val121 ? _augval119 : _val121;
                    }
                    var _child122 = _b97._right8;
                    if (!(_child122 == null)) {
                        var _val123 = _child122._min_ay13;
                        _augval119 = _augval119 < _val123 ? _augval119 : _val123;
                    }
                    _b97._min_ay13 = _augval119;
                    /* _max_ay24 is max of ay2 */
                    var _augval124 = _b97.ay2;
                    var _child125 = _b97._left7;
                    if (!(_child125 == null)) {
                        var _val126 = _child125._max_ay24;
                        _augval124 = _augval124 < _val126 ? _val126 : _augval124;
                    }
                    var _child127 = _b97._right8;
                    if (!(_child127 == null)) {
                        var _val128 = _child127._max_ay24;
                        _augval124 = _augval124 < _val128 ? _val128 : _augval124;
                    }
                    _b97._max_ay24 = _augval124;
                    _b97._height10 = 1 + ((_b97._left7 == null ? -1 : _b97._left7._height10) > (_b97._right8 ==
                            null ? -1 : _b97._right8._height10) ? _b97._left7 == null ? -1 : _b97._left7
                        ._height10 : _b97._right8 == null ? -1 : _b97._right8._height10);
                    if (!(_b97._parent9 == null)) {
                        /* _min_ax12 is min of ax1 */
                        var _augval129 = _b97._parent9.ax1;
                        var _child130 = _b97._parent9._left7;
                        if (!(_child130 == null)) {
                            var _val131 = _child130._min_ax12;
                            _augval129 = _augval129 < _val131 ? _augval129 : _val131;
                        }
                        var _child132 = _b97._parent9._right8;
                        if (!(_child132 == null)) {
                            var _val133 = _child132._min_ax12;
                            _augval129 = _augval129 < _val133 ? _augval129 : _val133;
                        }
                        _b97._parent9._min_ax12 = _augval129;
                        /* _min_ay13 is min of ay1 */
                        var _augval134 = _b97._parent9.ay1;
                        var _child135 = _b97._parent9._left7;
                        if (!(_child135 == null)) {
                            var _val136 = _child135._min_ay13;
                            _augval134 = _augval134 < _val136 ? _augval134 : _val136;
                        }
                        var _child137 = _b97._parent9._right8;
                        if (!(_child137 == null)) {
                            var _val138 = _child137._min_ay13;
                            _augval134 = _augval134 < _val138 ? _augval134 : _val138;
                        }
                        _b97._parent9._min_ay13 = _augval134;
                        /* _max_ay24 is max of ay2 */
                        var _augval139 = _b97._parent9.ay2;
                        var _child140 = _b97._parent9._left7;
                        if (!(_child140 == null)) {
                            var _val141 = _child140._max_ay24;
                            _augval139 = _augval139 < _val141 ? _val141 : _augval139;
                        }
                        var _child142 = _b97._parent9._right8;
                        if (!(_child142 == null)) {
                            var _val143 = _child142._max_ay24;
                            _augval139 = _augval139 < _val143 ? _val143 : _augval139;
                        }
                        _b97._parent9._max_ay24 = _augval139;
                        _b97._parent9._height10 = 1 + ((_b97._parent9._left7 == null ? -1 : _b97._parent9._left7
                                ._height10) > (_b97._parent9._right8 == null ? -1 : _b97._parent9._right8
                                ._height10) ? _b97._parent9._left7 == null ? -1 : _b97._parent9._left7
                            ._height10 : _b97._parent9._right8 == null ? -1 : _b97._parent9._right8._height10);
                    } else {
                        this._root1 = _b97;
                    }
                }
                /* rotate (_cursor94)._left7 */
                var _a144 = _cursor94;
                var _b145 = _a144._left7;
                var _c146 = _b145._right8;
                /* replace _a144 with _b145 in (_a144)._parent9 */
                if (!(_a144._parent9 == null)) {
                    if (_a144._parent9._left7 == _a144) {
                        _a144._parent9._left7 = _b145;
                    } else {
                        _a144._parent9._right8 = _b145;
                    }
                }
                if (!(_b145 == null)) {
                    _b145._parent9 = _a144._parent9;
                }
                /* replace _c146 with _a144 in _b145 */
                _b145._right8 = _a144;
                if (!(_a144 == null)) {
                    _a144._parent9 = _b145;
                }
                /* replace _b145 with _c146 in _a144 */
                _a144._left7 = _c146;
                if (!(_c146 == null)) {
                    _c146._parent9 = _a144;
                }
                /* _min_ax12 is min of ax1 */
                var _augval147 = _a144.ax1;
                var _child148 = _a144._left7;
                if (!(_child148 == null)) {
                    var _val149 = _child148._min_ax12;
                    _augval147 = _augval147 < _val149 ? _augval147 : _val149;
                }
                var _child150 = _a144._right8;
                if (!(_child150 == null)) {
                    var _val151 = _child150._min_ax12;
                    _augval147 = _augval147 < _val151 ? _augval147 : _val151;
                }
                _a144._min_ax12 = _augval147;
                /* _min_ay13 is min of ay1 */
                var _augval152 = _a144.ay1;
                var _child153 = _a144._left7;
                if (!(_child153 == null)) {
                    var _val154 = _child153._min_ay13;
                    _augval152 = _augval152 < _val154 ? _augval152 : _val154;
                }
                var _child155 = _a144._right8;
                if (!(_child155 == null)) {
                    var _val156 = _child155._min_ay13;
                    _augval152 = _augval152 < _val156 ? _augval152 : _val156;
                }
                _a144._min_ay13 = _augval152;
                /* _max_ay24 is max of ay2 */
                var _augval157 = _a144.ay2;
                var _child158 = _a144._left7;
                if (!(_child158 == null)) {
                    var _val159 = _child158._max_ay24;
                    _augval157 = _augval157 < _val159 ? _val159 : _augval157;
                }
                var _child160 = _a144._right8;
                if (!(_child160 == null)) {
                    var _val161 = _child160._max_ay24;
                    _augval157 = _augval157 < _val161 ? _val161 : _augval157;
                }
                _a144._max_ay24 = _augval157;
                _a144._height10 = 1 + ((_a144._left7 == null ? -1 : _a144._left7._height10) > (_a144._right8 ==
                        null ? -1 : _a144._right8._height10) ? _a144._left7 == null ? -1 : _a144._left7
                    ._height10 : _a144._right8 == null ? -1 : _a144._right8._height10);
                /* _min_ax12 is min of ax1 */
                var _augval162 = _b145.ax1;
                var _child163 = _b145._left7;
                if (!(_child163 == null)) {
                    var _val164 = _child163._min_ax12;
                    _augval162 = _augval162 < _val164 ? _augval162 : _val164;
                }
                var _child165 = _b145._right8;
                if (!(_child165 == null)) {
                    var _val166 = _child165._min_ax12;
                    _augval162 = _augval162 < _val166 ? _augval162 : _val166;
                }
                _b145._min_ax12 = _augval162;
                /* _min_ay13 is min of ay1 */
                var _augval167 = _b145.ay1;
                var _child168 = _b145._left7;
                if (!(_child168 == null)) {
                    var _val169 = _child168._min_ay13;
                    _augval167 = _augval167 < _val169 ? _augval167 : _val169;
                }
                var _child170 = _b145._right8;
                if (!(_child170 == null)) {
                    var _val171 = _child170._min_ay13;
                    _augval167 = _augval167 < _val171 ? _augval167 : _val171;
                }
                _b145._min_ay13 = _augval167;
                /* _max_ay24 is max of ay2 */
                var _augval172 = _b145.ay2;
                var _child173 = _b145._left7;
                if (!(_child173 == null)) {
                    var _val174 = _child173._max_ay24;
                    _augval172 = _augval172 < _val174 ? _val174 : _augval172;
                }
                var _child175 = _b145._right8;
                if (!(_child175 == null)) {
                    var _val176 = _child175._max_ay24;
                    _augval172 = _augval172 < _val176 ? _val176 : _augval172;
                }
                _b145._max_ay24 = _augval172;
                _b145._height10 = 1 + ((_b145._left7 == null ? -1 : _b145._left7._height10) > (_b145._right8 ==
                        null ? -1 : _b145._right8._height10) ? _b145._left7 == null ? -1 : _b145._left7
                    ._height10 : _b145._right8 == null ? -1 : _b145._right8._height10);
                if (!(_b145._parent9 == null)) {
                    /* _min_ax12 is min of ax1 */
                    var _augval177 = _b145._parent9.ax1;
                    var _child178 = _b145._parent9._left7;
                    if (!(_child178 == null)) {
                        var _val179 = _child178._min_ax12;
                        _augval177 = _augval177 < _val179 ? _augval177 : _val179;
                    }
                    var _child180 = _b145._parent9._right8;
                    if (!(_child180 == null)) {
                        var _val181 = _child180._min_ax12;
                        _augval177 = _augval177 < _val181 ? _augval177 : _val181;
                    }
                    _b145._parent9._min_ax12 = _augval177;
                    /* _min_ay13 is min of ay1 */
                    var _augval182 = _b145._parent9.ay1;
                    var _child183 = _b145._parent9._left7;
                    if (!(_child183 == null)) {
                        var _val184 = _child183._min_ay13;
                        _augval182 = _augval182 < _val184 ? _augval182 : _val184;
                    }
                    var _child185 = _b145._parent9._right8;
                    if (!(_child185 == null)) {
                        var _val186 = _child185._min_ay13;
                        _augval182 = _augval182 < _val186 ? _augval182 : _val186;
                    }
                    _b145._parent9._min_ay13 = _augval182;
                    /* _max_ay24 is max of ay2 */
                    var _augval187 = _b145._parent9.ay2;
                    var _child188 = _b145._parent9._left7;
                    if (!(_child188 == null)) {
                        var _val189 = _child188._max_ay24;
                        _augval187 = _augval187 < _val189 ? _val189 : _augval187;
                    }
                    var _child190 = _b145._parent9._right8;
                    if (!(_child190 == null)) {
                        var _val191 = _child190._max_ay24;
                        _augval187 = _augval187 < _val191 ? _val191 : _augval187;
                    }
                    _b145._parent9._max_ay24 = _augval187;
                    _b145._parent9._height10 = 1 + ((_b145._parent9._left7 == null ? -1 : _b145._parent9._left7
                            ._height10) > (_b145._parent9._right8 == null ? -1 : _b145._parent9._right8
                            ._height10) ? _b145._parent9._left7 == null ? -1 : _b145._parent9._left7._height10 :
                        _b145._parent9._right8 == null ? -1 : _b145._parent9._right8._height10);
                } else {
                    this._root1 = _b145;
                }
                _cursor94 = _cursor94._parent9;
            } else if (_imbalance95 < -1) {
                if (
                    (_cursor94._right8._left7 == null ? -1 : _cursor94._right8._left7._height10) > (_cursor94
                        ._right8._right8 == null ? -1 : _cursor94._right8._right8._height10)) {
                    /* rotate ((_cursor94)._right8)._left7 */
                    var _a192 = _cursor94._right8;
                    var _b193 = _a192._left7;
                    var _c194 = _b193._right8;
                    /* replace _a192 with _b193 in (_a192)._parent9 */
                    if (!(_a192._parent9 == null)) {
                        if (_a192._parent9._left7 == _a192) {
                            _a192._parent9._left7 = _b193;
                        } else {
                            _a192._parent9._right8 = _b193;
                        }
                    }
                    if (!(_b193 == null)) {
                        _b193._parent9 = _a192._parent9;
                    }
                    /* replace _c194 with _a192 in _b193 */
                    _b193._right8 = _a192;
                    if (!(_a192 == null)) {
                        _a192._parent9 = _b193;
                    }
                    /* replace _b193 with _c194 in _a192 */
                    _a192._left7 = _c194;
                    if (!(_c194 == null)) {
                        _c194._parent9 = _a192;
                    }
                    /* _min_ax12 is min of ax1 */
                    var _augval195 = _a192.ax1;
                    var _child196 = _a192._left7;
                    if (!(_child196 == null)) {
                        var _val197 = _child196._min_ax12;
                        _augval195 = _augval195 < _val197 ? _augval195 : _val197;
                    }
                    var _child198 = _a192._right8;
                    if (!(_child198 == null)) {
                        var _val199 = _child198._min_ax12;
                        _augval195 = _augval195 < _val199 ? _augval195 : _val199;
                    }
                    _a192._min_ax12 = _augval195;
                    /* _min_ay13 is min of ay1 */
                    var _augval200 = _a192.ay1;
                    var _child201 = _a192._left7;
                    if (!(_child201 == null)) {
                        var _val202 = _child201._min_ay13;
                        _augval200 = _augval200 < _val202 ? _augval200 : _val202;
                    }
                    var _child203 = _a192._right8;
                    if (!(_child203 == null)) {
                        var _val204 = _child203._min_ay13;
                        _augval200 = _augval200 < _val204 ? _augval200 : _val204;
                    }
                    _a192._min_ay13 = _augval200;
                    /* _max_ay24 is max of ay2 */
                    var _augval205 = _a192.ay2;
                    var _child206 = _a192._left7;
                    if (!(_child206 == null)) {
                        var _val207 = _child206._max_ay24;
                        _augval205 = _augval205 < _val207 ? _val207 : _augval205;
                    }
                    var _child208 = _a192._right8;
                    if (!(_child208 == null)) {
                        var _val209 = _child208._max_ay24;
                        _augval205 = _augval205 < _val209 ? _val209 : _augval205;
                    }
                    _a192._max_ay24 = _augval205;
                    _a192._height10 = 1 + ((_a192._left7 == null ? -1 : _a192._left7._height10) > (_a192._right8 ==
                            null ? -1 : _a192._right8._height10) ? _a192._left7 == null ? -1 : _a192._left7
                        ._height10 : _a192._right8 == null ? -1 : _a192._right8._height10);
                    /* _min_ax12 is min of ax1 */
                    var _augval210 = _b193.ax1;
                    var _child211 = _b193._left7;
                    if (!(_child211 == null)) {
                        var _val212 = _child211._min_ax12;
                        _augval210 = _augval210 < _val212 ? _augval210 : _val212;
                    }
                    var _child213 = _b193._right8;
                    if (!(_child213 == null)) {
                        var _val214 = _child213._min_ax12;
                        _augval210 = _augval210 < _val214 ? _augval210 : _val214;
                    }
                    _b193._min_ax12 = _augval210;
                    /* _min_ay13 is min of ay1 */
                    var _augval215 = _b193.ay1;
                    var _child216 = _b193._left7;
                    if (!(_child216 == null)) {
                        var _val217 = _child216._min_ay13;
                        _augval215 = _augval215 < _val217 ? _augval215 : _val217;
                    }
                    var _child218 = _b193._right8;
                    if (!(_child218 == null)) {
                        var _val219 = _child218._min_ay13;
                        _augval215 = _augval215 < _val219 ? _augval215 : _val219;
                    }
                    _b193._min_ay13 = _augval215;
                    /* _max_ay24 is max of ay2 */
                    var _augval220 = _b193.ay2;
                    var _child221 = _b193._left7;
                    if (!(_child221 == null)) {
                        var _val222 = _child221._max_ay24;
                        _augval220 = _augval220 < _val222 ? _val222 : _augval220;
                    }
                    var _child223 = _b193._right8;
                    if (!(_child223 == null)) {
                        var _val224 = _child223._max_ay24;
                        _augval220 = _augval220 < _val224 ? _val224 : _augval220;
                    }
                    _b193._max_ay24 = _augval220;
                    _b193._height10 = 1 + ((_b193._left7 == null ? -1 : _b193._left7._height10) > (_b193._right8 ==
                            null ? -1 : _b193._right8._height10) ? _b193._left7 == null ? -1 : _b193._left7
                        ._height10 : _b193._right8 == null ? -1 : _b193._right8._height10);
                    if (!(_b193._parent9 == null)) {
                        /* _min_ax12 is min of ax1 */
                        var _augval225 = _b193._parent9.ax1;
                        var _child226 = _b193._parent9._left7;
                        if (!(_child226 == null)) {
                            var _val227 = _child226._min_ax12;
                            _augval225 = _augval225 < _val227 ? _augval225 : _val227;
                        }
                        var _child228 = _b193._parent9._right8;
                        if (!(_child228 == null)) {
                            var _val229 = _child228._min_ax12;
                            _augval225 = _augval225 < _val229 ? _augval225 : _val229;
                        }
                        _b193._parent9._min_ax12 = _augval225;
                        /* _min_ay13 is min of ay1 */
                        var _augval230 = _b193._parent9.ay1;
                        var _child231 = _b193._parent9._left7;
                        if (!(_child231 == null)) {
                            var _val232 = _child231._min_ay13;
                            _augval230 = _augval230 < _val232 ? _augval230 : _val232;
                        }
                        var _child233 = _b193._parent9._right8;
                        if (!(_child233 == null)) {
                            var _val234 = _child233._min_ay13;
                            _augval230 = _augval230 < _val234 ? _augval230 : _val234;
                        }
                        _b193._parent9._min_ay13 = _augval230;
                        /* _max_ay24 is max of ay2 */
                        var _augval235 = _b193._parent9.ay2;
                        var _child236 = _b193._parent9._left7;
                        if (!(_child236 == null)) {
                            var _val237 = _child236._max_ay24;
                            _augval235 = _augval235 < _val237 ? _val237 : _augval235;
                        }
                        var _child238 = _b193._parent9._right8;
                        if (!(_child238 == null)) {
                            var _val239 = _child238._max_ay24;
                            _augval235 = _augval235 < _val239 ? _val239 : _augval235;
                        }
                        _b193._parent9._max_ay24 = _augval235;
                        _b193._parent9._height10 = 1 + ((_b193._parent9._left7 == null ? -1 : _b193._parent9._left7
                                ._height10) > (_b193._parent9._right8 == null ? -1 : _b193._parent9._right8
                                ._height10) ? _b193._parent9._left7 == null ? -1 : _b193._parent9._left7
                            ._height10 : _b193._parent9._right8 == null ? -1 : _b193._parent9._right8._height10);
                    } else {
                        this._root1 = _b193;
                    }
                }
                /* rotate (_cursor94)._right8 */
                var _a240 = _cursor94;
                var _b241 = _a240._right8;
                var _c242 = _b241._left7;
                /* replace _a240 with _b241 in (_a240)._parent9 */
                if (!(_a240._parent9 == null)) {
                    if (_a240._parent9._left7 == _a240) {
                        _a240._parent9._left7 = _b241;
                    } else {
                        _a240._parent9._right8 = _b241;
                    }
                }
                if (!(_b241 == null)) {
                    _b241._parent9 = _a240._parent9;
                }
                /* replace _c242 with _a240 in _b241 */
                _b241._left7 = _a240;
                if (!(_a240 == null)) {
                    _a240._parent9 = _b241;
                }
                /* replace _b241 with _c242 in _a240 */
                _a240._right8 = _c242;
                if (!(_c242 == null)) {
                    _c242._parent9 = _a240;
                }
                /* _min_ax12 is min of ax1 */
                var _augval243 = _a240.ax1;
                var _child244 = _a240._left7;
                if (!(_child244 == null)) {
                    var _val245 = _child244._min_ax12;
                    _augval243 = _augval243 < _val245 ? _augval243 : _val245;
                }
                var _child246 = _a240._right8;
                if (!(_child246 == null)) {
                    var _val247 = _child246._min_ax12;
                    _augval243 = _augval243 < _val247 ? _augval243 : _val247;
                }
                _a240._min_ax12 = _augval243;
                /* _min_ay13 is min of ay1 */
                var _augval248 = _a240.ay1;
                var _child249 = _a240._left7;
                if (!(_child249 == null)) {
                    var _val250 = _child249._min_ay13;
                    _augval248 = _augval248 < _val250 ? _augval248 : _val250;
                }
                var _child251 = _a240._right8;
                if (!(_child251 == null)) {
                    var _val252 = _child251._min_ay13;
                    _augval248 = _augval248 < _val252 ? _augval248 : _val252;
                }
                _a240._min_ay13 = _augval248;
                /* _max_ay24 is max of ay2 */
                var _augval253 = _a240.ay2;
                var _child254 = _a240._left7;
                if (!(_child254 == null)) {
                    var _val255 = _child254._max_ay24;
                    _augval253 = _augval253 < _val255 ? _val255 : _augval253;
                }
                var _child256 = _a240._right8;
                if (!(_child256 == null)) {
                    var _val257 = _child256._max_ay24;
                    _augval253 = _augval253 < _val257 ? _val257 : _augval253;
                }
                _a240._max_ay24 = _augval253;
                _a240._height10 = 1 + ((_a240._left7 == null ? -1 : _a240._left7._height10) > (_a240._right8 ==
                        null ? -1 : _a240._right8._height10) ? _a240._left7 == null ? -1 : _a240._left7
                    ._height10 : _a240._right8 == null ? -1 : _a240._right8._height10);
                /* _min_ax12 is min of ax1 */
                var _augval258 = _b241.ax1;
                var _child259 = _b241._left7;
                if (!(_child259 == null)) {
                    var _val260 = _child259._min_ax12;
                    _augval258 = _augval258 < _val260 ? _augval258 : _val260;
                }
                var _child261 = _b241._right8;
                if (!(_child261 == null)) {
                    var _val262 = _child261._min_ax12;
                    _augval258 = _augval258 < _val262 ? _augval258 : _val262;
                }
                _b241._min_ax12 = _augval258;
                /* _min_ay13 is min of ay1 */
                var _augval263 = _b241.ay1;
                var _child264 = _b241._left7;
                if (!(_child264 == null)) {
                    var _val265 = _child264._min_ay13;
                    _augval263 = _augval263 < _val265 ? _augval263 : _val265;
                }
                var _child266 = _b241._right8;
                if (!(_child266 == null)) {
                    var _val267 = _child266._min_ay13;
                    _augval263 = _augval263 < _val267 ? _augval263 : _val267;
                }
                _b241._min_ay13 = _augval263;
                /* _max_ay24 is max of ay2 */
                var _augval268 = _b241.ay2;
                var _child269 = _b241._left7;
                if (!(_child269 == null)) {
                    var _val270 = _child269._max_ay24;
                    _augval268 = _augval268 < _val270 ? _val270 : _augval268;
                }
                var _child271 = _b241._right8;
                if (!(_child271 == null)) {
                    var _val272 = _child271._max_ay24;
                    _augval268 = _augval268 < _val272 ? _val272 : _augval268;
                }
                _b241._max_ay24 = _augval268;
                _b241._height10 = 1 + ((_b241._left7 == null ? -1 : _b241._left7._height10) > (_b241._right8 ==
                        null ? -1 : _b241._right8._height10) ? _b241._left7 == null ? -1 : _b241._left7
                    ._height10 : _b241._right8 == null ? -1 : _b241._right8._height10);
                if (!(_b241._parent9 == null)) {
                    /* _min_ax12 is min of ax1 */
                    var _augval273 = _b241._parent9.ax1;
                    var _child274 = _b241._parent9._left7;
                    if (!(_child274 == null)) {
                        var _val275 = _child274._min_ax12;
                        _augval273 = _augval273 < _val275 ? _augval273 : _val275;
                    }
                    var _child276 = _b241._parent9._right8;
                    if (!(_child276 == null)) {
                        var _val277 = _child276._min_ax12;
                        _augval273 = _augval273 < _val277 ? _augval273 : _val277;
                    }
                    _b241._parent9._min_ax12 = _augval273;
                    /* _min_ay13 is min of ay1 */
                    var _augval278 = _b241._parent9.ay1;
                    var _child279 = _b241._parent9._left7;
                    if (!(_child279 == null)) {
                        var _val280 = _child279._min_ay13;
                        _augval278 = _augval278 < _val280 ? _augval278 : _val280;
                    }
                    var _child281 = _b241._parent9._right8;
                    if (!(_child281 == null)) {
                        var _val282 = _child281._min_ay13;
                        _augval278 = _augval278 < _val282 ? _augval278 : _val282;
                    }
                    _b241._parent9._min_ay13 = _augval278;
                    /* _max_ay24 is max of ay2 */
                    var _augval283 = _b241._parent9.ay2;
                    var _child284 = _b241._parent9._left7;
                    if (!(_child284 == null)) {
                        var _val285 = _child284._max_ay24;
                        _augval283 = _augval283 < _val285 ? _val285 : _augval283;
                    }
                    var _child286 = _b241._parent9._right8;
                    if (!(_child286 == null)) {
                        var _val287 = _child286._max_ay24;
                        _augval283 = _augval283 < _val287 ? _val287 : _augval283;
                    }
                    _b241._parent9._max_ay24 = _augval283;
                    _b241._parent9._height10 = 1 + ((_b241._parent9._left7 == null ? -1 : _b241._parent9._left7
                            ._height10) > (_b241._parent9._right8 == null ? -1 : _b241._parent9._right8
                            ._height10) ? _b241._parent9._left7 == null ? -1 : _b241._parent9._left7._height10 :
                        _b241._parent9._right8 == null ? -1 : _b241._parent9._right8._height10);
                } else {
                    this._root1 = _b241;
                }
                _cursor94 = _cursor94._parent9;
            }
        }
    };
    RectangleHolder.prototype.remove = function (x) {
        --this.my_size;
        var _parent288 = x._parent9;
        var _left289 = x._left7;
        var _right290 = x._right8;
        var _new_x291;
        if (_left289 == null && _right290 == null) {
            _new_x291 = null;
            /* replace x with _new_x291 in _parent288 */
            if (!(_parent288 == null)) {
                if (_parent288._left7 == x) {
                    _parent288._left7 = _new_x291;
                } else {
                    _parent288._right8 = _new_x291;
                }
            }
            if (!(_new_x291 == null)) {
                _new_x291._parent9 = _parent288;
            }
        } else if (!(_left289 == null) && _right290 == null) {
            _new_x291 = _left289;
            /* replace x with _new_x291 in _parent288 */
            if (!(_parent288 == null)) {
                if (_parent288._left7 == x) {
                    _parent288._left7 = _new_x291;
                } else {
                    _parent288._right8 = _new_x291;
                }
            }
            if (!(_new_x291 == null)) {
                _new_x291._parent9 = _parent288;
            }
        } else if (_left289 == null && !(_right290 == null)) {
            _new_x291 = _right290;
            /* replace x with _new_x291 in _parent288 */
            if (!(_parent288 == null)) {
                if (_parent288._left7 == x) {
                    _parent288._left7 = _new_x291;
                } else {
                    _parent288._right8 = _new_x291;
                }
            }
            if (!(_new_x291 == null)) {
                _new_x291._parent9 = _parent288;
            }
        } else {
            var _root292 = x._right8;
            var _x293 = _root292;
            var _descend294 = true;
            var _from_left295 = true;
            while (true) {
                if (_x293 == null) {
                    _x293 = null;
                    break;
                }
                if (_descend294) {
                    /* too small? */
                    if (false) {
                        if (!(_x293._right8 == null) && true) {
                            if (_x293 == _root292) {
                                _root292 = _x293._right8;
                            }
                            _x293 = _x293._right8;
                        } else if (_x293 == _root292) {
                            _x293 = null;
                            break;
                        } else {
                            _descend294 = false;
                            _from_left295 = !(_x293._parent9 == null) && _x293 == _x293._parent9._left7;
                            _x293 = _x293._parent9;
                        }
                    } else if (!(_x293._left7 == null) && true) {
                        _x293 = _x293._left7;
                        /* too large? */
                    } else if (false) {
                        if (_x293 == _root292) {
                            _x293 = null;
                            break;
                        } else {
                            _descend294 = false;
                            _from_left295 = !(_x293._parent9 == null) && _x293 == _x293._parent9._left7;
                            _x293 = _x293._parent9;
                        }
                        /* node ok? */
                    } else if (true) {
                        break;
                    } else if (_x293 == _root292) {
                        _root292 = _x293._right8;
                        _x293 = _x293._right8;
                    } else {
                        if (!(_x293._right8 == null) && true) {
                            if (_x293 == _root292) {
                                _root292 = _x293._right8;
                            }
                            _x293 = _x293._right8;
                        } else {
                            _descend294 = false;
                            _from_left295 = !(_x293._parent9 == null) && _x293 == _x293._parent9._left7;
                            _x293 = _x293._parent9;
                        }
                    }
                } else if (_from_left295) {
                    if (false) {
                        _x293 = null;
                        break;
                    } else if (true) {
                        break;
                    } else if (!(_x293._right8 == null) && true) {
                        _descend294 = true;
                        if (_x293 == _root292) {
                            _root292 = _x293._right8;
                        }
                        _x293 = _x293._right8;
                    } else if (_x293 == _root292) {
                        _x293 = null;
                        break;
                    } else {
                        _descend294 = false;
                        _from_left295 = !(_x293._parent9 == null) && _x293 == _x293._parent9._left7;
                        _x293 = _x293._parent9;
                    }
                } else {
                    if (_x293 == _root292) {
                        _x293 = null;
                        break;
                    } else {
                        _descend294 = false;
                        _from_left295 = !(_x293._parent9 == null) && _x293 == _x293._parent9._left7;
                        _x293 = _x293._parent9;
                    }
                }
            }
            _new_x291 = _x293;
            var _mp296 = _x293._parent9;
            var _mr297 = _x293._right8;
            /* replace _x293 with _mr297 in _mp296 */
            if (!(_mp296 == null)) {
                if (_mp296._left7 == _x293) {
                    _mp296._left7 = _mr297;
                } else {
                    _mp296._right8 = _mr297;
                }
            }
            if (!(_mr297 == null)) {
                _mr297._parent9 = _mp296;
            }
            /* replace x with _x293 in _parent288 */
            if (!(_parent288 == null)) {
                if (_parent288._left7 == x) {
                    _parent288._left7 = _x293;
                } else {
                    _parent288._right8 = _x293;
                }
            }
            if (!(_x293 == null)) {
                _x293._parent9 = _parent288;
            }
            /* replace null with _left289 in _x293 */
            _x293._left7 = _left289;
            if (!(_left289 == null)) {
                _left289._parent9 = _x293;
            }
            /* replace _mr297 with (x)._right8 in _x293 */
            _x293._right8 = x._right8;
            if (!(x._right8 == null)) {
                x._right8._parent9 = _x293;
            }
            /* _min_ax12 is min of ax1 */
            var _augval298 = _x293.ax1;
            var _child299 = _x293._left7;
            if (!(_child299 == null)) {
                var _val300 = _child299._min_ax12;
                _augval298 = _augval298 < _val300 ? _augval298 : _val300;
            }
            var _child301 = _x293._right8;
            if (!(_child301 == null)) {
                var _val302 = _child301._min_ax12;
                _augval298 = _augval298 < _val302 ? _augval298 : _val302;
            }
            _x293._min_ax12 = _augval298;
            /* _min_ay13 is min of ay1 */
            var _augval303 = _x293.ay1;
            var _child304 = _x293._left7;
            if (!(_child304 == null)) {
                var _val305 = _child304._min_ay13;
                _augval303 = _augval303 < _val305 ? _augval303 : _val305;
            }
            var _child306 = _x293._right8;
            if (!(_child306 == null)) {
                var _val307 = _child306._min_ay13;
                _augval303 = _augval303 < _val307 ? _augval303 : _val307;
            }
            _x293._min_ay13 = _augval303;
            /* _max_ay24 is max of ay2 */
            var _augval308 = _x293.ay2;
            var _child309 = _x293._left7;
            if (!(_child309 == null)) {
                var _val310 = _child309._max_ay24;
                _augval308 = _augval308 < _val310 ? _val310 : _augval308;
            }
            var _child311 = _x293._right8;
            if (!(_child311 == null)) {
                var _val312 = _child311._max_ay24;
                _augval308 = _augval308 < _val312 ? _val312 : _augval308;
            }
            _x293._max_ay24 = _augval308;
            _x293._height10 = 1 + ((_x293._left7 == null ? -1 : _x293._left7._height10) > (_x293._right8 == null ? -
                    1 : _x293._right8._height10) ? _x293._left7 == null ? -1 : _x293._left7._height10 : _x293
                ._right8 == null ? -1 : _x293._right8._height10);
            var _cursor313 = _mp296;
            var _changed314 = true;
            while (_changed314 && !(_cursor313 == _parent288)) {
                var _old__min_ax12315 = _cursor313._min_ax12;
                var _old__min_ay13316 = _cursor313._min_ay13;
                var _old__max_ay24317 = _cursor313._max_ay24;
                var _old_height318 = _cursor313._height10;
                /* _min_ax12 is min of ax1 */
                var _augval319 = _cursor313.ax1;
                var _child320 = _cursor313._left7;
                if (!(_child320 == null)) {
                    var _val321 = _child320._min_ax12;
                    _augval319 = _augval319 < _val321 ? _augval319 : _val321;
                }
                var _child322 = _cursor313._right8;
                if (!(_child322 == null)) {
                    var _val323 = _child322._min_ax12;
                    _augval319 = _augval319 < _val323 ? _augval319 : _val323;
                }
                _cursor313._min_ax12 = _augval319;
                /* _min_ay13 is min of ay1 */
                var _augval324 = _cursor313.ay1;
                var _child325 = _cursor313._left7;
                if (!(_child325 == null)) {
                    var _val326 = _child325._min_ay13;
                    _augval324 = _augval324 < _val326 ? _augval324 : _val326;
                }
                var _child327 = _cursor313._right8;
                if (!(_child327 == null)) {
                    var _val328 = _child327._min_ay13;
                    _augval324 = _augval324 < _val328 ? _augval324 : _val328;
                }
                _cursor313._min_ay13 = _augval324;
                /* _max_ay24 is max of ay2 */
                var _augval329 = _cursor313.ay2;
                var _child330 = _cursor313._left7;
                if (!(_child330 == null)) {
                    var _val331 = _child330._max_ay24;
                    _augval329 = _augval329 < _val331 ? _val331 : _augval329;
                }
                var _child332 = _cursor313._right8;
                if (!(_child332 == null)) {
                    var _val333 = _child332._max_ay24;
                    _augval329 = _augval329 < _val333 ? _val333 : _augval329;
                }
                _cursor313._max_ay24 = _augval329;
                _cursor313._height10 = 1 + ((_cursor313._left7 == null ? -1 : _cursor313._left7._height10) > (
                        _cursor313._right8 == null ? -1 : _cursor313._right8._height10) ? _cursor313._left7 ==
                    null ? -1 : _cursor313._left7._height10 : _cursor313._right8 == null ? -1 : _cursor313
                    ._right8._height10);
                _changed314 = false;
                _changed314 = _changed314 || !(_old__min_ax12315 == _cursor313._min_ax12);
                _changed314 = _changed314 || !(_old__min_ay13316 == _cursor313._min_ay13);
                _changed314 = _changed314 || !(_old__max_ay24317 == _cursor313._max_ay24);
                _changed314 = _changed314 || !(_old_height318 == _cursor313._height10);
                _cursor313 = _cursor313._parent9;
            }
        }
        var _cursor334 = _parent288;
        var _changed335 = true;
        while (_changed335 && !(_cursor334 == null)) {
            var _old__min_ax12336 = _cursor334._min_ax12;
            var _old__min_ay13337 = _cursor334._min_ay13;
            var _old__max_ay24338 = _cursor334._max_ay24;
            var _old_height339 = _cursor334._height10;
            /* _min_ax12 is min of ax1 */
            var _augval340 = _cursor334.ax1;
            var _child341 = _cursor334._left7;
            if (!(_child341 == null)) {
                var _val342 = _child341._min_ax12;
                _augval340 = _augval340 < _val342 ? _augval340 : _val342;
            }
            var _child343 = _cursor334._right8;
            if (!(_child343 == null)) {
                var _val344 = _child343._min_ax12;
                _augval340 = _augval340 < _val344 ? _augval340 : _val344;
            }
            _cursor334._min_ax12 = _augval340;
            /* _min_ay13 is min of ay1 */
            var _augval345 = _cursor334.ay1;
            var _child346 = _cursor334._left7;
            if (!(_child346 == null)) {
                var _val347 = _child346._min_ay13;
                _augval345 = _augval345 < _val347 ? _augval345 : _val347;
            }
            var _child348 = _cursor334._right8;
            if (!(_child348 == null)) {
                var _val349 = _child348._min_ay13;
                _augval345 = _augval345 < _val349 ? _augval345 : _val349;
            }
            _cursor334._min_ay13 = _augval345;
            /* _max_ay24 is max of ay2 */
            var _augval350 = _cursor334.ay2;
            var _child351 = _cursor334._left7;
            if (!(_child351 == null)) {
                var _val352 = _child351._max_ay24;
                _augval350 = _augval350 < _val352 ? _val352 : _augval350;
            }
            var _child353 = _cursor334._right8;
            if (!(_child353 == null)) {
                var _val354 = _child353._max_ay24;
                _augval350 = _augval350 < _val354 ? _val354 : _augval350;
            }
            _cursor334._max_ay24 = _augval350;
            _cursor334._height10 = 1 + ((_cursor334._left7 == null ? -1 : _cursor334._left7._height10) > (_cursor334
                    ._right8 == null ? -1 : _cursor334._right8._height10) ? _cursor334._left7 == null ? -1 :
                _cursor334._left7._height10 : _cursor334._right8 == null ? -1 : _cursor334._right8._height10);
            _changed335 = false;
            _changed335 = _changed335 || !(_old__min_ax12336 == _cursor334._min_ax12);
            _changed335 = _changed335 || !(_old__min_ay13337 == _cursor334._min_ay13);
            _changed335 = _changed335 || !(_old__max_ay24338 == _cursor334._max_ay24);
            _changed335 = _changed335 || !(_old_height339 == _cursor334._height10);
            _cursor334 = _cursor334._parent9;
        }
        if (this._root1 == x) {
            this._root1 = _new_x291;
        }
    };
    RectangleHolder.prototype.updateAx1 = function (__x, new_val) {
        if (__x.ax1 != new_val) {
            /* _min_ax12 is min of ax1 */
            var _augval355 = new_val;
            var _child356 = __x._left7;
            if (!(_child356 == null)) {
                var _val357 = _child356._min_ax12;
                _augval355 = _augval355 < _val357 ? _augval355 : _val357;
            }
            var _child358 = __x._right8;
            if (!(_child358 == null)) {
                var _val359 = _child358._min_ax12;
                _augval355 = _augval355 < _val359 ? _augval355 : _val359;
            }
            __x._min_ax12 = _augval355;
            var _cursor360 = __x._parent9;
            var _changed361 = true;
            while (_changed361 && !(_cursor360 == null)) {
                var _old__min_ax12362 = _cursor360._min_ax12;
                var _old_height363 = _cursor360._height10;
                /* _min_ax12 is min of ax1 */
                var _augval364 = _cursor360.ax1;
                var _child365 = _cursor360._left7;
                if (!(_child365 == null)) {
                    var _val366 = _child365._min_ax12;
                    _augval364 = _augval364 < _val366 ? _augval364 : _val366;
                }
                var _child367 = _cursor360._right8;
                if (!(_child367 == null)) {
                    var _val368 = _child367._min_ax12;
                    _augval364 = _augval364 < _val368 ? _augval364 : _val368;
                }
                _cursor360._min_ax12 = _augval364;
                _cursor360._height10 = 1 + ((_cursor360._left7 == null ? -1 : _cursor360._left7._height10) > (
                        _cursor360._right8 == null ? -1 : _cursor360._right8._height10) ? _cursor360._left7 ==
                    null ? -1 : _cursor360._left7._height10 : _cursor360._right8 == null ? -1 : _cursor360
                    ._right8._height10);
                _changed361 = false;
                _changed361 = _changed361 || !(_old__min_ax12362 == _cursor360._min_ax12);
                _changed361 = _changed361 || !(_old_height363 == _cursor360._height10);
                _cursor360 = _cursor360._parent9;
            }
            __x.ax1 = new_val;
        }
    };
    RectangleHolder.prototype.updateAy1 = function (__x, new_val) {
        if (__x.ay1 != new_val) {
            /* _min_ay13 is min of ay1 */
            var _augval369 = new_val;
            var _child370 = __x._left7;
            if (!(_child370 == null)) {
                var _val371 = _child370._min_ay13;
                _augval369 = _augval369 < _val371 ? _augval369 : _val371;
            }
            var _child372 = __x._right8;
            if (!(_child372 == null)) {
                var _val373 = _child372._min_ay13;
                _augval369 = _augval369 < _val373 ? _augval369 : _val373;
            }
            __x._min_ay13 = _augval369;
            var _cursor374 = __x._parent9;
            var _changed375 = true;
            while (_changed375 && !(_cursor374 == null)) {
                var _old__min_ay13376 = _cursor374._min_ay13;
                var _old_height377 = _cursor374._height10;
                /* _min_ay13 is min of ay1 */
                var _augval378 = _cursor374.ay1;
                var _child379 = _cursor374._left7;
                if (!(_child379 == null)) {
                    var _val380 = _child379._min_ay13;
                    _augval378 = _augval378 < _val380 ? _augval378 : _val380;
                }
                var _child381 = _cursor374._right8;
                if (!(_child381 == null)) {
                    var _val382 = _child381._min_ay13;
                    _augval378 = _augval378 < _val382 ? _augval378 : _val382;
                }
                _cursor374._min_ay13 = _augval378;
                _cursor374._height10 = 1 + ((_cursor374._left7 == null ? -1 : _cursor374._left7._height10) > (
                        _cursor374._right8 == null ? -1 : _cursor374._right8._height10) ? _cursor374._left7 ==
                    null ? -1 : _cursor374._left7._height10 : _cursor374._right8 == null ? -1 : _cursor374
                    ._right8._height10);
                _changed375 = false;
                _changed375 = _changed375 || !(_old__min_ay13376 == _cursor374._min_ay13);
                _changed375 = _changed375 || !(_old_height377 == _cursor374._height10);
                _cursor374 = _cursor374._parent9;
            }
            __x.ay1 = new_val;
        }
    };
    RectangleHolder.prototype.updateAx2 = function (__x, new_val) {
        if (__x.ax2 != new_val) {
            var _parent383 = __x._parent9;
            var _left384 = __x._left7;
            var _right385 = __x._right8;
            var _new_x386;
            if (_left384 == null && _right385 == null) {
                _new_x386 = null;
                /* replace __x with _new_x386 in _parent383 */
                if (!(_parent383 == null)) {
                    if (_parent383._left7 == __x) {
                        _parent383._left7 = _new_x386;
                    } else {
                        _parent383._right8 = _new_x386;
                    }
                }
                if (!(_new_x386 == null)) {
                    _new_x386._parent9 = _parent383;
                }
            } else if (!(_left384 == null) && _right385 == null) {
                _new_x386 = _left384;
                /* replace __x with _new_x386 in _parent383 */
                if (!(_parent383 == null)) {
                    if (_parent383._left7 == __x) {
                        _parent383._left7 = _new_x386;
                    } else {
                        _parent383._right8 = _new_x386;
                    }
                }
                if (!(_new_x386 == null)) {
                    _new_x386._parent9 = _parent383;
                }
            } else if (_left384 == null && !(_right385 == null)) {
                _new_x386 = _right385;
                /* replace __x with _new_x386 in _parent383 */
                if (!(_parent383 == null)) {
                    if (_parent383._left7 == __x) {
                        _parent383._left7 = _new_x386;
                    } else {
                        _parent383._right8 = _new_x386;
                    }
                }
                if (!(_new_x386 == null)) {
                    _new_x386._parent9 = _parent383;
                }
            } else {
                var _root387 = __x._right8;
                var _x388 = _root387;
                var _descend389 = true;
                var _from_left390 = true;
                while (true) {
                    if (_x388 == null) {
                        _x388 = null;
                        break;
                    }
                    if (_descend389) {
                        /* too small? */
                        if (false) {
                            if (!(_x388._right8 == null) && true) {
                                if (_x388 == _root387) {
                                    _root387 = _x388._right8;
                                }
                                _x388 = _x388._right8;
                            } else if (_x388 == _root387) {
                                _x388 = null;
                                break;
                            } else {
                                _descend389 = false;
                                _from_left390 = !(_x388._parent9 == null) && _x388 == _x388._parent9._left7;
                                _x388 = _x388._parent9;
                            }
                        } else if (!(_x388._left7 == null) && true) {
                            _x388 = _x388._left7;
                            /* too large? */
                        } else if (false) {
                            if (_x388 == _root387) {
                                _x388 = null;
                                break;
                            } else {
                                _descend389 = false;
                                _from_left390 = !(_x388._parent9 == null) && _x388 == _x388._parent9._left7;
                                _x388 = _x388._parent9;
                            }
                            /* node ok? */
                        } else if (true) {
                            break;
                        } else if (_x388 == _root387) {
                            _root387 = _x388._right8;
                            _x388 = _x388._right8;
                        } else {
                            if (!(_x388._right8 == null) && true) {
                                if (_x388 == _root387) {
                                    _root387 = _x388._right8;
                                }
                                _x388 = _x388._right8;
                            } else {
                                _descend389 = false;
                                _from_left390 = !(_x388._parent9 == null) && _x388 == _x388._parent9._left7;
                                _x388 = _x388._parent9;
                            }
                        }
                    } else if (_from_left390) {
                        if (false) {
                            _x388 = null;
                            break;
                        } else if (true) {
                            break;
                        } else if (!(_x388._right8 == null) && true) {
                            _descend389 = true;
                            if (_x388 == _root387) {
                                _root387 = _x388._right8;
                            }
                            _x388 = _x388._right8;
                        } else if (_x388 == _root387) {
                            _x388 = null;
                            break;
                        } else {
                            _descend389 = false;
                            _from_left390 = !(_x388._parent9 == null) && _x388 == _x388._parent9._left7;
                            _x388 = _x388._parent9;
                        }
                    } else {
                        if (_x388 == _root387) {
                            _x388 = null;
                            break;
                        } else {
                            _descend389 = false;
                            _from_left390 = !(_x388._parent9 == null) && _x388 == _x388._parent9._left7;
                            _x388 = _x388._parent9;
                        }
                    }
                }
                _new_x386 = _x388;
                var _mp391 = _x388._parent9;
                var _mr392 = _x388._right8;
                /* replace _x388 with _mr392 in _mp391 */
                if (!(_mp391 == null)) {
                    if (_mp391._left7 == _x388) {
                        _mp391._left7 = _mr392;
                    } else {
                        _mp391._right8 = _mr392;
                    }
                }
                if (!(_mr392 == null)) {
                    _mr392._parent9 = _mp391;
                }
                /* replace __x with _x388 in _parent383 */
                if (!(_parent383 == null)) {
                    if (_parent383._left7 == __x) {
                        _parent383._left7 = _x388;
                    } else {
                        _parent383._right8 = _x388;
                    }
                }
                if (!(_x388 == null)) {
                    _x388._parent9 = _parent383;
                }
                /* replace null with _left384 in _x388 */
                _x388._left7 = _left384;
                if (!(_left384 == null)) {
                    _left384._parent9 = _x388;
                }
                /* replace _mr392 with (__x)._right8 in _x388 */
                _x388._right8 = __x._right8;
                if (!(__x._right8 == null)) {
                    __x._right8._parent9 = _x388;
                }
                /* _min_ax12 is min of ax1 */
                var _augval393 = _x388.ax1;
                var _child394 = _x388._left7;
                if (!(_child394 == null)) {
                    var _val395 = _child394._min_ax12;
                    _augval393 = _augval393 < _val395 ? _augval393 : _val395;
                }
                var _child396 = _x388._right8;
                if (!(_child396 == null)) {
                    var _val397 = _child396._min_ax12;
                    _augval393 = _augval393 < _val397 ? _augval393 : _val397;
                }
                _x388._min_ax12 = _augval393;
                /* _min_ay13 is min of ay1 */
                var _augval398 = _x388.ay1;
                var _child399 = _x388._left7;
                if (!(_child399 == null)) {
                    var _val400 = _child399._min_ay13;
                    _augval398 = _augval398 < _val400 ? _augval398 : _val400;
                }
                var _child401 = _x388._right8;
                if (!(_child401 == null)) {
                    var _val402 = _child401._min_ay13;
                    _augval398 = _augval398 < _val402 ? _augval398 : _val402;
                }
                _x388._min_ay13 = _augval398;
                /* _max_ay24 is max of ay2 */
                var _augval403 = _x388.ay2;
                var _child404 = _x388._left7;
                if (!(_child404 == null)) {
                    var _val405 = _child404._max_ay24;
                    _augval403 = _augval403 < _val405 ? _val405 : _augval403;
                }
                var _child406 = _x388._right8;
                if (!(_child406 == null)) {
                    var _val407 = _child406._max_ay24;
                    _augval403 = _augval403 < _val407 ? _val407 : _augval403;
                }
                _x388._max_ay24 = _augval403;
                _x388._height10 = 1 + ((_x388._left7 == null ? -1 : _x388._left7._height10) > (_x388._right8 ==
                        null ? -1 : _x388._right8._height10) ? _x388._left7 == null ? -1 : _x388._left7
                    ._height10 : _x388._right8 == null ? -1 : _x388._right8._height10);
                var _cursor408 = _mp391;
                var _changed409 = true;
                while (_changed409 && !(_cursor408 == _parent383)) {
                    var _old__min_ax12410 = _cursor408._min_ax12;
                    var _old__min_ay13411 = _cursor408._min_ay13;
                    var _old__max_ay24412 = _cursor408._max_ay24;
                    var _old_height413 = _cursor408._height10;
                    /* _min_ax12 is min of ax1 */
                    var _augval414 = _cursor408.ax1;
                    var _child415 = _cursor408._left7;
                    if (!(_child415 == null)) {
                        var _val416 = _child415._min_ax12;
                        _augval414 = _augval414 < _val416 ? _augval414 : _val416;
                    }
                    var _child417 = _cursor408._right8;
                    if (!(_child417 == null)) {
                        var _val418 = _child417._min_ax12;
                        _augval414 = _augval414 < _val418 ? _augval414 : _val418;
                    }
                    _cursor408._min_ax12 = _augval414;
                    /* _min_ay13 is min of ay1 */
                    var _augval419 = _cursor408.ay1;
                    var _child420 = _cursor408._left7;
                    if (!(_child420 == null)) {
                        var _val421 = _child420._min_ay13;
                        _augval419 = _augval419 < _val421 ? _augval419 : _val421;
                    }
                    var _child422 = _cursor408._right8;
                    if (!(_child422 == null)) {
                        var _val423 = _child422._min_ay13;
                        _augval419 = _augval419 < _val423 ? _augval419 : _val423;
                    }
                    _cursor408._min_ay13 = _augval419;
                    /* _max_ay24 is max of ay2 */
                    var _augval424 = _cursor408.ay2;
                    var _child425 = _cursor408._left7;
                    if (!(_child425 == null)) {
                        var _val426 = _child425._max_ay24;
                        _augval424 = _augval424 < _val426 ? _val426 : _augval424;
                    }
                    var _child427 = _cursor408._right8;
                    if (!(_child427 == null)) {
                        var _val428 = _child427._max_ay24;
                        _augval424 = _augval424 < _val428 ? _val428 : _augval424;
                    }
                    _cursor408._max_ay24 = _augval424;
                    _cursor408._height10 = 1 + ((_cursor408._left7 == null ? -1 : _cursor408._left7._height10) > (
                            _cursor408._right8 == null ? -1 : _cursor408._right8._height10) ? _cursor408
                        ._left7 == null ? -1 : _cursor408._left7._height10 : _cursor408._right8 == null ? -1 :
                        _cursor408._right8._height10);
                    _changed409 = false;
                    _changed409 = _changed409 || !(_old__min_ax12410 == _cursor408._min_ax12);
                    _changed409 = _changed409 || !(_old__min_ay13411 == _cursor408._min_ay13);
                    _changed409 = _changed409 || !(_old__max_ay24412 == _cursor408._max_ay24);
                    _changed409 = _changed409 || !(_old_height413 == _cursor408._height10);
                    _cursor408 = _cursor408._parent9;
                }
            }
            var _cursor429 = _parent383;
            var _changed430 = true;
            while (_changed430 && !(_cursor429 == null)) {
                var _old__min_ax12431 = _cursor429._min_ax12;
                var _old__min_ay13432 = _cursor429._min_ay13;
                var _old__max_ay24433 = _cursor429._max_ay24;
                var _old_height434 = _cursor429._height10;
                /* _min_ax12 is min of ax1 */
                var _augval435 = _cursor429.ax1;
                var _child436 = _cursor429._left7;
                if (!(_child436 == null)) {
                    var _val437 = _child436._min_ax12;
                    _augval435 = _augval435 < _val437 ? _augval435 : _val437;
                }
                var _child438 = _cursor429._right8;
                if (!(_child438 == null)) {
                    var _val439 = _child438._min_ax12;
                    _augval435 = _augval435 < _val439 ? _augval435 : _val439;
                }
                _cursor429._min_ax12 = _augval435;
                /* _min_ay13 is min of ay1 */
                var _augval440 = _cursor429.ay1;
                var _child441 = _cursor429._left7;
                if (!(_child441 == null)) {
                    var _val442 = _child441._min_ay13;
                    _augval440 = _augval440 < _val442 ? _augval440 : _val442;
                }
                var _child443 = _cursor429._right8;
                if (!(_child443 == null)) {
                    var _val444 = _child443._min_ay13;
                    _augval440 = _augval440 < _val444 ? _augval440 : _val444;
                }
                _cursor429._min_ay13 = _augval440;
                /* _max_ay24 is max of ay2 */
                var _augval445 = _cursor429.ay2;
                var _child446 = _cursor429._left7;
                if (!(_child446 == null)) {
                    var _val447 = _child446._max_ay24;
                    _augval445 = _augval445 < _val447 ? _val447 : _augval445;
                }
                var _child448 = _cursor429._right8;
                if (!(_child448 == null)) {
                    var _val449 = _child448._max_ay24;
                    _augval445 = _augval445 < _val449 ? _val449 : _augval445;
                }
                _cursor429._max_ay24 = _augval445;
                _cursor429._height10 = 1 + ((_cursor429._left7 == null ? -1 : _cursor429._left7._height10) > (
                        _cursor429._right8 == null ? -1 : _cursor429._right8._height10) ? _cursor429._left7 ==
                    null ? -1 : _cursor429._left7._height10 : _cursor429._right8 == null ? -1 : _cursor429
                    ._right8._height10);
                _changed430 = false;
                _changed430 = _changed430 || !(_old__min_ax12431 == _cursor429._min_ax12);
                _changed430 = _changed430 || !(_old__min_ay13432 == _cursor429._min_ay13);
                _changed430 = _changed430 || !(_old__max_ay24433 == _cursor429._max_ay24);
                _changed430 = _changed430 || !(_old_height434 == _cursor429._height10);
                _cursor429 = _cursor429._parent9;
            }
            if (this._root1 == __x) {
                this._root1 = _new_x386;
            }
            __x._left7 = null;
            __x._right8 = null;
            __x._min_ax12 = __x.ax1;
            __x._min_ay13 = __x.ay1;
            __x._max_ay24 = __x.ay2;
            __x._height10 = 0;
            var _previous450 = null;
            var _current451 = this._root1;
            var _is_left452 = false;
            while (!(_current451 == null)) {
                _previous450 = _current451;
                if (new_val < _current451.ax2) {
                    _current451 = _current451._left7;
                    _is_left452 = true;
                } else {
                    _current451 = _current451._right8;
                    _is_left452 = false;
                }
            }
            if (_previous450 == null) {
                this._root1 = __x;
            } else {
                __x._parent9 = _previous450;
                if (_is_left452) {
                    _previous450._left7 = __x;
                } else {
                    _previous450._right8 = __x;
                }
            }
            var _cursor453 = __x._parent9;
            var _changed454 = true;
            while (_changed454 && !(_cursor453 == null)) {
                var _old__min_ax12455 = _cursor453._min_ax12;
                var _old__min_ay13456 = _cursor453._min_ay13;
                var _old__max_ay24457 = _cursor453._max_ay24;
                var _old_height458 = _cursor453._height10;
                /* _min_ax12 is min of ax1 */
                var _augval459 = _cursor453.ax1;
                var _child460 = _cursor453._left7;
                if (!(_child460 == null)) {
                    var _val461 = _child460._min_ax12;
                    _augval459 = _augval459 < _val461 ? _augval459 : _val461;
                }
                var _child462 = _cursor453._right8;
                if (!(_child462 == null)) {
                    var _val463 = _child462._min_ax12;
                    _augval459 = _augval459 < _val463 ? _augval459 : _val463;
                }
                _cursor453._min_ax12 = _augval459;
                /* _min_ay13 is min of ay1 */
                var _augval464 = _cursor453.ay1;
                var _child465 = _cursor453._left7;
                if (!(_child465 == null)) {
                    var _val466 = _child465._min_ay13;
                    _augval464 = _augval464 < _val466 ? _augval464 : _val466;
                }
                var _child467 = _cursor453._right8;
                if (!(_child467 == null)) {
                    var _val468 = _child467._min_ay13;
                    _augval464 = _augval464 < _val468 ? _augval464 : _val468;
                }
                _cursor453._min_ay13 = _augval464;
                /* _max_ay24 is max of ay2 */
                var _augval469 = _cursor453.ay2;
                var _child470 = _cursor453._left7;
                if (!(_child470 == null)) {
                    var _val471 = _child470._max_ay24;
                    _augval469 = _augval469 < _val471 ? _val471 : _augval469;
                }
                var _child472 = _cursor453._right8;
                if (!(_child472 == null)) {
                    var _val473 = _child472._max_ay24;
                    _augval469 = _augval469 < _val473 ? _val473 : _augval469;
                }
                _cursor453._max_ay24 = _augval469;
                _cursor453._height10 = 1 + ((_cursor453._left7 == null ? -1 : _cursor453._left7._height10) > (
                        _cursor453._right8 == null ? -1 : _cursor453._right8._height10) ? _cursor453._left7 ==
                    null ? -1 : _cursor453._left7._height10 : _cursor453._right8 == null ? -1 : _cursor453
                    ._right8._height10);
                _changed454 = false;
                _changed454 = _changed454 || !(_old__min_ax12455 == _cursor453._min_ax12);
                _changed454 = _changed454 || !(_old__min_ay13456 == _cursor453._min_ay13);
                _changed454 = _changed454 || !(_old__max_ay24457 == _cursor453._max_ay24);
                _changed454 = _changed454 || !(_old_height458 == _cursor453._height10);
                _cursor453 = _cursor453._parent9;
            }
            /* rebalance AVL tree */
            var _cursor474 = __x;
            var _imbalance475;
            while (!(_cursor474._parent9 == null)) {
                _cursor474 = _cursor474._parent9;
                _cursor474._height10 = 1 + ((_cursor474._left7 == null ? -1 : _cursor474._left7._height10) > (
                        _cursor474._right8 == null ? -1 : _cursor474._right8._height10) ? _cursor474._left7 ==
                    null ? -1 : _cursor474._left7._height10 : _cursor474._right8 == null ? -1 : _cursor474
                    ._right8._height10);
                _imbalance475 = (_cursor474._left7 == null ? -1 : _cursor474._left7._height10) - (_cursor474
                    ._right8 == null ? -1 : _cursor474._right8._height10);
                if (_imbalance475 > 1) {
                    if (
                        (_cursor474._left7._left7 == null ? -1 : _cursor474._left7._left7._height10) < (_cursor474
                            ._left7._right8 == null ? -1 : _cursor474._left7._right8._height10)) {
                        /* rotate ((_cursor474)._left7)._right8 */
                        var _a476 = _cursor474._left7;
                        var _b477 = _a476._right8;
                        var _c478 = _b477._left7;
                        /* replace _a476 with _b477 in (_a476)._parent9 */
                        if (!(_a476._parent9 == null)) {
                            if (_a476._parent9._left7 == _a476) {
                                _a476._parent9._left7 = _b477;
                            } else {
                                _a476._parent9._right8 = _b477;
                            }
                        }
                        if (!(_b477 == null)) {
                            _b477._parent9 = _a476._parent9;
                        }
                        /* replace _c478 with _a476 in _b477 */
                        _b477._left7 = _a476;
                        if (!(_a476 == null)) {
                            _a476._parent9 = _b477;
                        }
                        /* replace _b477 with _c478 in _a476 */
                        _a476._right8 = _c478;
                        if (!(_c478 == null)) {
                            _c478._parent9 = _a476;
                        }
                        /* _min_ax12 is min of ax1 */
                        var _augval479 = _a476.ax1;
                        var _child480 = _a476._left7;
                        if (!(_child480 == null)) {
                            var _val481 = _child480._min_ax12;
                            _augval479 = _augval479 < _val481 ? _augval479 : _val481;
                        }
                        var _child482 = _a476._right8;
                        if (!(_child482 == null)) {
                            var _val483 = _child482._min_ax12;
                            _augval479 = _augval479 < _val483 ? _augval479 : _val483;
                        }
                        _a476._min_ax12 = _augval479;
                        /* _min_ay13 is min of ay1 */
                        var _augval484 = _a476.ay1;
                        var _child485 = _a476._left7;
                        if (!(_child485 == null)) {
                            var _val486 = _child485._min_ay13;
                            _augval484 = _augval484 < _val486 ? _augval484 : _val486;
                        }
                        var _child487 = _a476._right8;
                        if (!(_child487 == null)) {
                            var _val488 = _child487._min_ay13;
                            _augval484 = _augval484 < _val488 ? _augval484 : _val488;
                        }
                        _a476._min_ay13 = _augval484;
                        /* _max_ay24 is max of ay2 */
                        var _augval489 = _a476.ay2;
                        var _child490 = _a476._left7;
                        if (!(_child490 == null)) {
                            var _val491 = _child490._max_ay24;
                            _augval489 = _augval489 < _val491 ? _val491 : _augval489;
                        }
                        var _child492 = _a476._right8;
                        if (!(_child492 == null)) {
                            var _val493 = _child492._max_ay24;
                            _augval489 = _augval489 < _val493 ? _val493 : _augval489;
                        }
                        _a476._max_ay24 = _augval489;
                        _a476._height10 = 1 + ((_a476._left7 == null ? -1 : _a476._left7._height10) > (_a476
                                ._right8 == null ? -1 : _a476._right8._height10) ? _a476._left7 == null ? -1 :
                            _a476._left7._height10 : _a476._right8 == null ? -1 : _a476._right8._height10);
                        /* _min_ax12 is min of ax1 */
                        var _augval494 = _b477.ax1;
                        var _child495 = _b477._left7;
                        if (!(_child495 == null)) {
                            var _val496 = _child495._min_ax12;
                            _augval494 = _augval494 < _val496 ? _augval494 : _val496;
                        }
                        var _child497 = _b477._right8;
                        if (!(_child497 == null)) {
                            var _val498 = _child497._min_ax12;
                            _augval494 = _augval494 < _val498 ? _augval494 : _val498;
                        }
                        _b477._min_ax12 = _augval494;
                        /* _min_ay13 is min of ay1 */
                        var _augval499 = _b477.ay1;
                        var _child500 = _b477._left7;
                        if (!(_child500 == null)) {
                            var _val501 = _child500._min_ay13;
                            _augval499 = _augval499 < _val501 ? _augval499 : _val501;
                        }
                        var _child502 = _b477._right8;
                        if (!(_child502 == null)) {
                            var _val503 = _child502._min_ay13;
                            _augval499 = _augval499 < _val503 ? _augval499 : _val503;
                        }
                        _b477._min_ay13 = _augval499;
                        /* _max_ay24 is max of ay2 */
                        var _augval504 = _b477.ay2;
                        var _child505 = _b477._left7;
                        if (!(_child505 == null)) {
                            var _val506 = _child505._max_ay24;
                            _augval504 = _augval504 < _val506 ? _val506 : _augval504;
                        }
                        var _child507 = _b477._right8;
                        if (!(_child507 == null)) {
                            var _val508 = _child507._max_ay24;
                            _augval504 = _augval504 < _val508 ? _val508 : _augval504;
                        }
                        _b477._max_ay24 = _augval504;
                        _b477._height10 = 1 + ((_b477._left7 == null ? -1 : _b477._left7._height10) > (_b477
                                ._right8 == null ? -1 : _b477._right8._height10) ? _b477._left7 == null ? -1 :
                            _b477._left7._height10 : _b477._right8 == null ? -1 : _b477._right8._height10);
                        if (!(_b477._parent9 == null)) {
                            /* _min_ax12 is min of ax1 */
                            var _augval509 = _b477._parent9.ax1;
                            var _child510 = _b477._parent9._left7;
                            if (!(_child510 == null)) {
                                var _val511 = _child510._min_ax12;
                                _augval509 = _augval509 < _val511 ? _augval509 : _val511;
                            }
                            var _child512 = _b477._parent9._right8;
                            if (!(_child512 == null)) {
                                var _val513 = _child512._min_ax12;
                                _augval509 = _augval509 < _val513 ? _augval509 : _val513;
                            }
                            _b477._parent9._min_ax12 = _augval509;
                            /* _min_ay13 is min of ay1 */
                            var _augval514 = _b477._parent9.ay1;
                            var _child515 = _b477._parent9._left7;
                            if (!(_child515 == null)) {
                                var _val516 = _child515._min_ay13;
                                _augval514 = _augval514 < _val516 ? _augval514 : _val516;
                            }
                            var _child517 = _b477._parent9._right8;
                            if (!(_child517 == null)) {
                                var _val518 = _child517._min_ay13;
                                _augval514 = _augval514 < _val518 ? _augval514 : _val518;
                            }
                            _b477._parent9._min_ay13 = _augval514;
                            /* _max_ay24 is max of ay2 */
                            var _augval519 = _b477._parent9.ay2;
                            var _child520 = _b477._parent9._left7;
                            if (!(_child520 == null)) {
                                var _val521 = _child520._max_ay24;
                                _augval519 = _augval519 < _val521 ? _val521 : _augval519;
                            }
                            var _child522 = _b477._parent9._right8;
                            if (!(_child522 == null)) {
                                var _val523 = _child522._max_ay24;
                                _augval519 = _augval519 < _val523 ? _val523 : _augval519;
                            }
                            _b477._parent9._max_ay24 = _augval519;
                            _b477._parent9._height10 = 1 + ((_b477._parent9._left7 == null ? -1 : _b477._parent9
                                    ._left7._height10) > (_b477._parent9._right8 == null ? -1 : _b477._parent9
                                    ._right8._height10) ? _b477._parent9._left7 == null ? -1 : _b477._parent9
                                ._left7._height10 : _b477._parent9._right8 == null ? -1 : _b477._parent9._right8
                                ._height10);
                        } else {
                            this._root1 = _b477;
                        }
                    }
                    /* rotate (_cursor474)._left7 */
                    var _a524 = _cursor474;
                    var _b525 = _a524._left7;
                    var _c526 = _b525._right8;
                    /* replace _a524 with _b525 in (_a524)._parent9 */
                    if (!(_a524._parent9 == null)) {
                        if (_a524._parent9._left7 == _a524) {
                            _a524._parent9._left7 = _b525;
                        } else {
                            _a524._parent9._right8 = _b525;
                        }
                    }
                    if (!(_b525 == null)) {
                        _b525._parent9 = _a524._parent9;
                    }
                    /* replace _c526 with _a524 in _b525 */
                    _b525._right8 = _a524;
                    if (!(_a524 == null)) {
                        _a524._parent9 = _b525;
                    }
                    /* replace _b525 with _c526 in _a524 */
                    _a524._left7 = _c526;
                    if (!(_c526 == null)) {
                        _c526._parent9 = _a524;
                    }
                    /* _min_ax12 is min of ax1 */
                    var _augval527 = _a524.ax1;
                    var _child528 = _a524._left7;
                    if (!(_child528 == null)) {
                        var _val529 = _child528._min_ax12;
                        _augval527 = _augval527 < _val529 ? _augval527 : _val529;
                    }
                    var _child530 = _a524._right8;
                    if (!(_child530 == null)) {
                        var _val531 = _child530._min_ax12;
                        _augval527 = _augval527 < _val531 ? _augval527 : _val531;
                    }
                    _a524._min_ax12 = _augval527;
                    /* _min_ay13 is min of ay1 */
                    var _augval532 = _a524.ay1;
                    var _child533 = _a524._left7;
                    if (!(_child533 == null)) {
                        var _val534 = _child533._min_ay13;
                        _augval532 = _augval532 < _val534 ? _augval532 : _val534;
                    }
                    var _child535 = _a524._right8;
                    if (!(_child535 == null)) {
                        var _val536 = _child535._min_ay13;
                        _augval532 = _augval532 < _val536 ? _augval532 : _val536;
                    }
                    _a524._min_ay13 = _augval532;
                    /* _max_ay24 is max of ay2 */
                    var _augval537 = _a524.ay2;
                    var _child538 = _a524._left7;
                    if (!(_child538 == null)) {
                        var _val539 = _child538._max_ay24;
                        _augval537 = _augval537 < _val539 ? _val539 : _augval537;
                    }
                    var _child540 = _a524._right8;
                    if (!(_child540 == null)) {
                        var _val541 = _child540._max_ay24;
                        _augval537 = _augval537 < _val541 ? _val541 : _augval537;
                    }
                    _a524._max_ay24 = _augval537;
                    _a524._height10 = 1 + ((_a524._left7 == null ? -1 : _a524._left7._height10) > (_a524._right8 ==
                            null ? -1 : _a524._right8._height10) ? _a524._left7 == null ? -1 : _a524._left7
                        ._height10 : _a524._right8 == null ? -1 : _a524._right8._height10);
                    /* _min_ax12 is min of ax1 */
                    var _augval542 = _b525.ax1;
                    var _child543 = _b525._left7;
                    if (!(_child543 == null)) {
                        var _val544 = _child543._min_ax12;
                        _augval542 = _augval542 < _val544 ? _augval542 : _val544;
                    }
                    var _child545 = _b525._right8;
                    if (!(_child545 == null)) {
                        var _val546 = _child545._min_ax12;
                        _augval542 = _augval542 < _val546 ? _augval542 : _val546;
                    }
                    _b525._min_ax12 = _augval542;
                    /* _min_ay13 is min of ay1 */
                    var _augval547 = _b525.ay1;
                    var _child548 = _b525._left7;
                    if (!(_child548 == null)) {
                        var _val549 = _child548._min_ay13;
                        _augval547 = _augval547 < _val549 ? _augval547 : _val549;
                    }
                    var _child550 = _b525._right8;
                    if (!(_child550 == null)) {
                        var _val551 = _child550._min_ay13;
                        _augval547 = _augval547 < _val551 ? _augval547 : _val551;
                    }
                    _b525._min_ay13 = _augval547;
                    /* _max_ay24 is max of ay2 */
                    var _augval552 = _b525.ay2;
                    var _child553 = _b525._left7;
                    if (!(_child553 == null)) {
                        var _val554 = _child553._max_ay24;
                        _augval552 = _augval552 < _val554 ? _val554 : _augval552;
                    }
                    var _child555 = _b525._right8;
                    if (!(_child555 == null)) {
                        var _val556 = _child555._max_ay24;
                        _augval552 = _augval552 < _val556 ? _val556 : _augval552;
                    }
                    _b525._max_ay24 = _augval552;
                    _b525._height10 = 1 + ((_b525._left7 == null ? -1 : _b525._left7._height10) > (_b525._right8 ==
                            null ? -1 : _b525._right8._height10) ? _b525._left7 == null ? -1 : _b525._left7
                        ._height10 : _b525._right8 == null ? -1 : _b525._right8._height10);
                    if (!(_b525._parent9 == null)) {
                        /* _min_ax12 is min of ax1 */
                        var _augval557 = _b525._parent9.ax1;
                        var _child558 = _b525._parent9._left7;
                        if (!(_child558 == null)) {
                            var _val559 = _child558._min_ax12;
                            _augval557 = _augval557 < _val559 ? _augval557 : _val559;
                        }
                        var _child560 = _b525._parent9._right8;
                        if (!(_child560 == null)) {
                            var _val561 = _child560._min_ax12;
                            _augval557 = _augval557 < _val561 ? _augval557 : _val561;
                        }
                        _b525._parent9._min_ax12 = _augval557;
                        /* _min_ay13 is min of ay1 */
                        var _augval562 = _b525._parent9.ay1;
                        var _child563 = _b525._parent9._left7;
                        if (!(_child563 == null)) {
                            var _val564 = _child563._min_ay13;
                            _augval562 = _augval562 < _val564 ? _augval562 : _val564;
                        }
                        var _child565 = _b525._parent9._right8;
                        if (!(_child565 == null)) {
                            var _val566 = _child565._min_ay13;
                            _augval562 = _augval562 < _val566 ? _augval562 : _val566;
                        }
                        _b525._parent9._min_ay13 = _augval562;
                        /* _max_ay24 is max of ay2 */
                        var _augval567 = _b525._parent9.ay2;
                        var _child568 = _b525._parent9._left7;
                        if (!(_child568 == null)) {
                            var _val569 = _child568._max_ay24;
                            _augval567 = _augval567 < _val569 ? _val569 : _augval567;
                        }
                        var _child570 = _b525._parent9._right8;
                        if (!(_child570 == null)) {
                            var _val571 = _child570._max_ay24;
                            _augval567 = _augval567 < _val571 ? _val571 : _augval567;
                        }
                        _b525._parent9._max_ay24 = _augval567;
                        _b525._parent9._height10 = 1 + ((_b525._parent9._left7 == null ? -1 : _b525._parent9._left7
                                ._height10) > (_b525._parent9._right8 == null ? -1 : _b525._parent9._right8
                                ._height10) ? _b525._parent9._left7 == null ? -1 : _b525._parent9._left7
                            ._height10 : _b525._parent9._right8 == null ? -1 : _b525._parent9._right8._height10);
                    } else {
                        this._root1 = _b525;
                    }
                    _cursor474 = _cursor474._parent9;
                } else if (_imbalance475 < -1) {
                    if (
                        (_cursor474._right8._left7 == null ? -1 : _cursor474._right8._left7._height10) > (_cursor474
                            ._right8._right8 == null ? -1 : _cursor474._right8._right8._height10)) {
                        /* rotate ((_cursor474)._right8)._left7 */
                        var _a572 = _cursor474._right8;
                        var _b573 = _a572._left7;
                        var _c574 = _b573._right8;
                        /* replace _a572 with _b573 in (_a572)._parent9 */
                        if (!(_a572._parent9 == null)) {
                            if (_a572._parent9._left7 == _a572) {
                                _a572._parent9._left7 = _b573;
                            } else {
                                _a572._parent9._right8 = _b573;
                            }
                        }
                        if (!(_b573 == null)) {
                            _b573._parent9 = _a572._parent9;
                        }
                        /* replace _c574 with _a572 in _b573 */
                        _b573._right8 = _a572;
                        if (!(_a572 == null)) {
                            _a572._parent9 = _b573;
                        }
                        /* replace _b573 with _c574 in _a572 */
                        _a572._left7 = _c574;
                        if (!(_c574 == null)) {
                            _c574._parent9 = _a572;
                        }
                        /* _min_ax12 is min of ax1 */
                        var _augval575 = _a572.ax1;
                        var _child576 = _a572._left7;
                        if (!(_child576 == null)) {
                            var _val577 = _child576._min_ax12;
                            _augval575 = _augval575 < _val577 ? _augval575 : _val577;
                        }
                        var _child578 = _a572._right8;
                        if (!(_child578 == null)) {
                            var _val579 = _child578._min_ax12;
                            _augval575 = _augval575 < _val579 ? _augval575 : _val579;
                        }
                        _a572._min_ax12 = _augval575;
                        /* _min_ay13 is min of ay1 */
                        var _augval580 = _a572.ay1;
                        var _child581 = _a572._left7;
                        if (!(_child581 == null)) {
                            var _val582 = _child581._min_ay13;
                            _augval580 = _augval580 < _val582 ? _augval580 : _val582;
                        }
                        var _child583 = _a572._right8;
                        if (!(_child583 == null)) {
                            var _val584 = _child583._min_ay13;
                            _augval580 = _augval580 < _val584 ? _augval580 : _val584;
                        }
                        _a572._min_ay13 = _augval580;
                        /* _max_ay24 is max of ay2 */
                        var _augval585 = _a572.ay2;
                        var _child586 = _a572._left7;
                        if (!(_child586 == null)) {
                            var _val587 = _child586._max_ay24;
                            _augval585 = _augval585 < _val587 ? _val587 : _augval585;
                        }
                        var _child588 = _a572._right8;
                        if (!(_child588 == null)) {
                            var _val589 = _child588._max_ay24;
                            _augval585 = _augval585 < _val589 ? _val589 : _augval585;
                        }
                        _a572._max_ay24 = _augval585;
                        _a572._height10 = 1 + ((_a572._left7 == null ? -1 : _a572._left7._height10) > (_a572
                                ._right8 == null ? -1 : _a572._right8._height10) ? _a572._left7 == null ? -1 :
                            _a572._left7._height10 : _a572._right8 == null ? -1 : _a572._right8._height10);
                        /* _min_ax12 is min of ax1 */
                        var _augval590 = _b573.ax1;
                        var _child591 = _b573._left7;
                        if (!(_child591 == null)) {
                            var _val592 = _child591._min_ax12;
                            _augval590 = _augval590 < _val592 ? _augval590 : _val592;
                        }
                        var _child593 = _b573._right8;
                        if (!(_child593 == null)) {
                            var _val594 = _child593._min_ax12;
                            _augval590 = _augval590 < _val594 ? _augval590 : _val594;
                        }
                        _b573._min_ax12 = _augval590;
                        /* _min_ay13 is min of ay1 */
                        var _augval595 = _b573.ay1;
                        var _child596 = _b573._left7;
                        if (!(_child596 == null)) {
                            var _val597 = _child596._min_ay13;
                            _augval595 = _augval595 < _val597 ? _augval595 : _val597;
                        }
                        var _child598 = _b573._right8;
                        if (!(_child598 == null)) {
                            var _val599 = _child598._min_ay13;
                            _augval595 = _augval595 < _val599 ? _augval595 : _val599;
                        }
                        _b573._min_ay13 = _augval595;
                        /* _max_ay24 is max of ay2 */
                        var _augval600 = _b573.ay2;
                        var _child601 = _b573._left7;
                        if (!(_child601 == null)) {
                            var _val602 = _child601._max_ay24;
                            _augval600 = _augval600 < _val602 ? _val602 : _augval600;
                        }
                        var _child603 = _b573._right8;
                        if (!(_child603 == null)) {
                            var _val604 = _child603._max_ay24;
                            _augval600 = _augval600 < _val604 ? _val604 : _augval600;
                        }
                        _b573._max_ay24 = _augval600;
                        _b573._height10 = 1 + ((_b573._left7 == null ? -1 : _b573._left7._height10) > (_b573
                                ._right8 == null ? -1 : _b573._right8._height10) ? _b573._left7 == null ? -1 :
                            _b573._left7._height10 : _b573._right8 == null ? -1 : _b573._right8._height10);
                        if (!(_b573._parent9 == null)) {
                            /* _min_ax12 is min of ax1 */
                            var _augval605 = _b573._parent9.ax1;
                            var _child606 = _b573._parent9._left7;
                            if (!(_child606 == null)) {
                                var _val607 = _child606._min_ax12;
                                _augval605 = _augval605 < _val607 ? _augval605 : _val607;
                            }
                            var _child608 = _b573._parent9._right8;
                            if (!(_child608 == null)) {
                                var _val609 = _child608._min_ax12;
                                _augval605 = _augval605 < _val609 ? _augval605 : _val609;
                            }
                            _b573._parent9._min_ax12 = _augval605;
                            /* _min_ay13 is min of ay1 */
                            var _augval610 = _b573._parent9.ay1;
                            var _child611 = _b573._parent9._left7;
                            if (!(_child611 == null)) {
                                var _val612 = _child611._min_ay13;
                                _augval610 = _augval610 < _val612 ? _augval610 : _val612;
                            }
                            var _child613 = _b573._parent9._right8;
                            if (!(_child613 == null)) {
                                var _val614 = _child613._min_ay13;
                                _augval610 = _augval610 < _val614 ? _augval610 : _val614;
                            }
                            _b573._parent9._min_ay13 = _augval610;
                            /* _max_ay24 is max of ay2 */
                            var _augval615 = _b573._parent9.ay2;
                            var _child616 = _b573._parent9._left7;
                            if (!(_child616 == null)) {
                                var _val617 = _child616._max_ay24;
                                _augval615 = _augval615 < _val617 ? _val617 : _augval615;
                            }
                            var _child618 = _b573._parent9._right8;
                            if (!(_child618 == null)) {
                                var _val619 = _child618._max_ay24;
                                _augval615 = _augval615 < _val619 ? _val619 : _augval615;
                            }
                            _b573._parent9._max_ay24 = _augval615;
                            _b573._parent9._height10 = 1 + ((_b573._parent9._left7 == null ? -1 : _b573._parent9
                                    ._left7._height10) > (_b573._parent9._right8 == null ? -1 : _b573._parent9
                                    ._right8._height10) ? _b573._parent9._left7 == null ? -1 : _b573._parent9
                                ._left7._height10 : _b573._parent9._right8 == null ? -1 : _b573._parent9._right8
                                ._height10);
                        } else {
                            this._root1 = _b573;
                        }
                    }
                    /* rotate (_cursor474)._right8 */
                    var _a620 = _cursor474;
                    var _b621 = _a620._right8;
                    var _c622 = _b621._left7;
                    /* replace _a620 with _b621 in (_a620)._parent9 */
                    if (!(_a620._parent9 == null)) {
                        if (_a620._parent9._left7 == _a620) {
                            _a620._parent9._left7 = _b621;
                        } else {
                            _a620._parent9._right8 = _b621;
                        }
                    }
                    if (!(_b621 == null)) {
                        _b621._parent9 = _a620._parent9;
                    }
                    /* replace _c622 with _a620 in _b621 */
                    _b621._left7 = _a620;
                    if (!(_a620 == null)) {
                        _a620._parent9 = _b621;
                    }
                    /* replace _b621 with _c622 in _a620 */
                    _a620._right8 = _c622;
                    if (!(_c622 == null)) {
                        _c622._parent9 = _a620;
                    }
                    /* _min_ax12 is min of ax1 */
                    var _augval623 = _a620.ax1;
                    var _child624 = _a620._left7;
                    if (!(_child624 == null)) {
                        var _val625 = _child624._min_ax12;
                        _augval623 = _augval623 < _val625 ? _augval623 : _val625;
                    }
                    var _child626 = _a620._right8;
                    if (!(_child626 == null)) {
                        var _val627 = _child626._min_ax12;
                        _augval623 = _augval623 < _val627 ? _augval623 : _val627;
                    }
                    _a620._min_ax12 = _augval623;
                    /* _min_ay13 is min of ay1 */
                    var _augval628 = _a620.ay1;
                    var _child629 = _a620._left7;
                    if (!(_child629 == null)) {
                        var _val630 = _child629._min_ay13;
                        _augval628 = _augval628 < _val630 ? _augval628 : _val630;
                    }
                    var _child631 = _a620._right8;
                    if (!(_child631 == null)) {
                        var _val632 = _child631._min_ay13;
                        _augval628 = _augval628 < _val632 ? _augval628 : _val632;
                    }
                    _a620._min_ay13 = _augval628;
                    /* _max_ay24 is max of ay2 */
                    var _augval633 = _a620.ay2;
                    var _child634 = _a620._left7;
                    if (!(_child634 == null)) {
                        var _val635 = _child634._max_ay24;
                        _augval633 = _augval633 < _val635 ? _val635 : _augval633;
                    }
                    var _child636 = _a620._right8;
                    if (!(_child636 == null)) {
                        var _val637 = _child636._max_ay24;
                        _augval633 = _augval633 < _val637 ? _val637 : _augval633;
                    }
                    _a620._max_ay24 = _augval633;
                    _a620._height10 = 1 + ((_a620._left7 == null ? -1 : _a620._left7._height10) > (_a620._right8 ==
                            null ? -1 : _a620._right8._height10) ? _a620._left7 == null ? -1 : _a620._left7
                        ._height10 : _a620._right8 == null ? -1 : _a620._right8._height10);
                    /* _min_ax12 is min of ax1 */
                    var _augval638 = _b621.ax1;
                    var _child639 = _b621._left7;
                    if (!(_child639 == null)) {
                        var _val640 = _child639._min_ax12;
                        _augval638 = _augval638 < _val640 ? _augval638 : _val640;
                    }
                    var _child641 = _b621._right8;
                    if (!(_child641 == null)) {
                        var _val642 = _child641._min_ax12;
                        _augval638 = _augval638 < _val642 ? _augval638 : _val642;
                    }
                    _b621._min_ax12 = _augval638;
                    /* _min_ay13 is min of ay1 */
                    var _augval643 = _b621.ay1;
                    var _child644 = _b621._left7;
                    if (!(_child644 == null)) {
                        var _val645 = _child644._min_ay13;
                        _augval643 = _augval643 < _val645 ? _augval643 : _val645;
                    }
                    var _child646 = _b621._right8;
                    if (!(_child646 == null)) {
                        var _val647 = _child646._min_ay13;
                        _augval643 = _augval643 < _val647 ? _augval643 : _val647;
                    }
                    _b621._min_ay13 = _augval643;
                    /* _max_ay24 is max of ay2 */
                    var _augval648 = _b621.ay2;
                    var _child649 = _b621._left7;
                    if (!(_child649 == null)) {
                        var _val650 = _child649._max_ay24;
                        _augval648 = _augval648 < _val650 ? _val650 : _augval648;
                    }
                    var _child651 = _b621._right8;
                    if (!(_child651 == null)) {
                        var _val652 = _child651._max_ay24;
                        _augval648 = _augval648 < _val652 ? _val652 : _augval648;
                    }
                    _b621._max_ay24 = _augval648;
                    _b621._height10 = 1 + ((_b621._left7 == null ? -1 : _b621._left7._height10) > (_b621._right8 ==
                            null ? -1 : _b621._right8._height10) ? _b621._left7 == null ? -1 : _b621._left7
                        ._height10 : _b621._right8 == null ? -1 : _b621._right8._height10);
                    if (!(_b621._parent9 == null)) {
                        /* _min_ax12 is min of ax1 */
                        var _augval653 = _b621._parent9.ax1;
                        var _child654 = _b621._parent9._left7;
                        if (!(_child654 == null)) {
                            var _val655 = _child654._min_ax12;
                            _augval653 = _augval653 < _val655 ? _augval653 : _val655;
                        }
                        var _child656 = _b621._parent9._right8;
                        if (!(_child656 == null)) {
                            var _val657 = _child656._min_ax12;
                            _augval653 = _augval653 < _val657 ? _augval653 : _val657;
                        }
                        _b621._parent9._min_ax12 = _augval653;
                        /* _min_ay13 is min of ay1 */
                        var _augval658 = _b621._parent9.ay1;
                        var _child659 = _b621._parent9._left7;
                        if (!(_child659 == null)) {
                            var _val660 = _child659._min_ay13;
                            _augval658 = _augval658 < _val660 ? _augval658 : _val660;
                        }
                        var _child661 = _b621._parent9._right8;
                        if (!(_child661 == null)) {
                            var _val662 = _child661._min_ay13;
                            _augval658 = _augval658 < _val662 ? _augval658 : _val662;
                        }
                        _b621._parent9._min_ay13 = _augval658;
                        /* _max_ay24 is max of ay2 */
                        var _augval663 = _b621._parent9.ay2;
                        var _child664 = _b621._parent9._left7;
                        if (!(_child664 == null)) {
                            var _val665 = _child664._max_ay24;
                            _augval663 = _augval663 < _val665 ? _val665 : _augval663;
                        }
                        var _child666 = _b621._parent9._right8;
                        if (!(_child666 == null)) {
                            var _val667 = _child666._max_ay24;
                            _augval663 = _augval663 < _val667 ? _val667 : _augval663;
                        }
                        _b621._parent9._max_ay24 = _augval663;
                        _b621._parent9._height10 = 1 + ((_b621._parent9._left7 == null ? -1 : _b621._parent9._left7
                                ._height10) > (_b621._parent9._right8 == null ? -1 : _b621._parent9._right8
                                ._height10) ? _b621._parent9._left7 == null ? -1 : _b621._parent9._left7
                            ._height10 : _b621._parent9._right8 == null ? -1 : _b621._parent9._right8._height10);
                    } else {
                        this._root1 = _b621;
                    }
                    _cursor474 = _cursor474._parent9;
                }
            }
            __x.ax2 = new_val;
        }
    };
    RectangleHolder.prototype.updateAy2 = function (__x, new_val) {
        if (__x.ay2 != new_val) {
            /* _max_ay24 is max of ay2 */
            var _augval668 = new_val;
            var _child669 = __x._left7;
            if (!(_child669 == null)) {
                var _val670 = _child669._max_ay24;
                _augval668 = _augval668 < _val670 ? _val670 : _augval668;
            }
            var _child671 = __x._right8;
            if (!(_child671 == null)) {
                var _val672 = _child671._max_ay24;
                _augval668 = _augval668 < _val672 ? _val672 : _augval668;
            }
            __x._max_ay24 = _augval668;
            var _cursor673 = __x._parent9;
            var _changed674 = true;
            while (_changed674 && !(_cursor673 == null)) {
                var _old__max_ay24675 = _cursor673._max_ay24;
                var _old_height676 = _cursor673._height10;
                /* _max_ay24 is max of ay2 */
                var _augval677 = _cursor673.ay2;
                var _child678 = _cursor673._left7;
                if (!(_child678 == null)) {
                    var _val679 = _child678._max_ay24;
                    _augval677 = _augval677 < _val679 ? _val679 : _augval677;
                }
                var _child680 = _cursor673._right8;
                if (!(_child680 == null)) {
                    var _val681 = _child680._max_ay24;
                    _augval677 = _augval677 < _val681 ? _val681 : _augval677;
                }
                _cursor673._max_ay24 = _augval677;
                _cursor673._height10 = 1 + ((_cursor673._left7 == null ? -1 : _cursor673._left7._height10) > (
                        _cursor673._right8 == null ? -1 : _cursor673._right8._height10) ? _cursor673._left7 ==
                    null ? -1 : _cursor673._left7._height10 : _cursor673._right8 == null ? -1 : _cursor673
                    ._right8._height10);
                _changed674 = false;
                _changed674 = _changed674 || !(_old__max_ay24675 == _cursor673._max_ay24);
                _changed674 = _changed674 || !(_old_height676 == _cursor673._height10);
                _cursor673 = _cursor673._parent9;
            }
            __x.ay2 = new_val;
        }
    };
    RectangleHolder.prototype.update = function (__x, ax1, ay1, ax2, ay2) {
        var _parent682 = __x._parent9;
        var _left683 = __x._left7;
        var _right684 = __x._right8;
        var _new_x685;
        if (_left683 == null && _right684 == null) {
            _new_x685 = null;
            /* replace __x with _new_x685 in _parent682 */
            if (!(_parent682 == null)) {
                if (_parent682._left7 == __x) {
                    _parent682._left7 = _new_x685;
                } else {
                    _parent682._right8 = _new_x685;
                }
            }
            if (!(_new_x685 == null)) {
                _new_x685._parent9 = _parent682;
            }
        } else if (!(_left683 == null) && _right684 == null) {
            _new_x685 = _left683;
            /* replace __x with _new_x685 in _parent682 */
            if (!(_parent682 == null)) {
                if (_parent682._left7 == __x) {
                    _parent682._left7 = _new_x685;
                } else {
                    _parent682._right8 = _new_x685;
                }
            }
            if (!(_new_x685 == null)) {
                _new_x685._parent9 = _parent682;
            }
        } else if (_left683 == null && !(_right684 == null)) {
            _new_x685 = _right684;
            /* replace __x with _new_x685 in _parent682 */
            if (!(_parent682 == null)) {
                if (_parent682._left7 == __x) {
                    _parent682._left7 = _new_x685;
                } else {
                    _parent682._right8 = _new_x685;
                }
            }
            if (!(_new_x685 == null)) {
                _new_x685._parent9 = _parent682;
            }
        } else {
            var _root686 = __x._right8;
            var _x687 = _root686;
            var _descend688 = true;
            var _from_left689 = true;
            while (true) {
                if (_x687 == null) {
                    _x687 = null;
                    break;
                }
                if (_descend688) {
                    /* too small? */
                    if (false) {
                        if (!(_x687._right8 == null) && true) {
                            if (_x687 == _root686) {
                                _root686 = _x687._right8;
                            }
                            _x687 = _x687._right8;
                        } else if (_x687 == _root686) {
                            _x687 = null;
                            break;
                        } else {
                            _descend688 = false;
                            _from_left689 = !(_x687._parent9 == null) && _x687 == _x687._parent9._left7;
                            _x687 = _x687._parent9;
                        }
                    } else if (!(_x687._left7 == null) && true) {
                        _x687 = _x687._left7;
                        /* too large? */
                    } else if (false) {
                        if (_x687 == _root686) {
                            _x687 = null;
                            break;
                        } else {
                            _descend688 = false;
                            _from_left689 = !(_x687._parent9 == null) && _x687 == _x687._parent9._left7;
                            _x687 = _x687._parent9;
                        }
                        /* node ok? */
                    } else if (true) {
                        break;
                    } else if (_x687 == _root686) {
                        _root686 = _x687._right8;
                        _x687 = _x687._right8;
                    } else {
                        if (!(_x687._right8 == null) && true) {
                            if (_x687 == _root686) {
                                _root686 = _x687._right8;
                            }
                            _x687 = _x687._right8;
                        } else {
                            _descend688 = false;
                            _from_left689 = !(_x687._parent9 == null) && _x687 == _x687._parent9._left7;
                            _x687 = _x687._parent9;
                        }
                    }
                } else if (_from_left689) {
                    if (false) {
                        _x687 = null;
                        break;
                    } else if (true) {
                        break;
                    } else if (!(_x687._right8 == null) && true) {
                        _descend688 = true;
                        if (_x687 == _root686) {
                            _root686 = _x687._right8;
                        }
                        _x687 = _x687._right8;
                    } else if (_x687 == _root686) {
                        _x687 = null;
                        break;
                    } else {
                        _descend688 = false;
                        _from_left689 = !(_x687._parent9 == null) && _x687 == _x687._parent9._left7;
                        _x687 = _x687._parent9;
                    }
                } else {
                    if (_x687 == _root686) {
                        _x687 = null;
                        break;
                    } else {
                        _descend688 = false;
                        _from_left689 = !(_x687._parent9 == null) && _x687 == _x687._parent9._left7;
                        _x687 = _x687._parent9;
                    }
                }
            }
            _new_x685 = _x687;
            var _mp690 = _x687._parent9;
            var _mr691 = _x687._right8;
            /* replace _x687 with _mr691 in _mp690 */
            if (!(_mp690 == null)) {
                if (_mp690._left7 == _x687) {
                    _mp690._left7 = _mr691;
                } else {
                    _mp690._right8 = _mr691;
                }
            }
            if (!(_mr691 == null)) {
                _mr691._parent9 = _mp690;
            }
            /* replace __x with _x687 in _parent682 */
            if (!(_parent682 == null)) {
                if (_parent682._left7 == __x) {
                    _parent682._left7 = _x687;
                } else {
                    _parent682._right8 = _x687;
                }
            }
            if (!(_x687 == null)) {
                _x687._parent9 = _parent682;
            }
            /* replace null with _left683 in _x687 */
            _x687._left7 = _left683;
            if (!(_left683 == null)) {
                _left683._parent9 = _x687;
            }
            /* replace _mr691 with (__x)._right8 in _x687 */
            _x687._right8 = __x._right8;
            if (!(__x._right8 == null)) {
                __x._right8._parent9 = _x687;
            }
            /* _min_ax12 is min of ax1 */
            var _augval692 = _x687.ax1;
            var _child693 = _x687._left7;
            if (!(_child693 == null)) {
                var _val694 = _child693._min_ax12;
                _augval692 = _augval692 < _val694 ? _augval692 : _val694;
            }
            var _child695 = _x687._right8;
            if (!(_child695 == null)) {
                var _val696 = _child695._min_ax12;
                _augval692 = _augval692 < _val696 ? _augval692 : _val696;
            }
            _x687._min_ax12 = _augval692;
            /* _min_ay13 is min of ay1 */
            var _augval697 = _x687.ay1;
            var _child698 = _x687._left7;
            if (!(_child698 == null)) {
                var _val699 = _child698._min_ay13;
                _augval697 = _augval697 < _val699 ? _augval697 : _val699;
            }
            var _child700 = _x687._right8;
            if (!(_child700 == null)) {
                var _val701 = _child700._min_ay13;
                _augval697 = _augval697 < _val701 ? _augval697 : _val701;
            }
            _x687._min_ay13 = _augval697;
            /* _max_ay24 is max of ay2 */
            var _augval702 = _x687.ay2;
            var _child703 = _x687._left7;
            if (!(_child703 == null)) {
                var _val704 = _child703._max_ay24;
                _augval702 = _augval702 < _val704 ? _val704 : _augval702;
            }
            var _child705 = _x687._right8;
            if (!(_child705 == null)) {
                var _val706 = _child705._max_ay24;
                _augval702 = _augval702 < _val706 ? _val706 : _augval702;
            }
            _x687._max_ay24 = _augval702;
            _x687._height10 = 1 + ((_x687._left7 == null ? -1 : _x687._left7._height10) > (_x687._right8 == null ? -
                    1 : _x687._right8._height10) ? _x687._left7 == null ? -1 : _x687._left7._height10 : _x687
                ._right8 == null ? -1 : _x687._right8._height10);
            var _cursor707 = _mp690;
            var _changed708 = true;
            while (_changed708 && !(_cursor707 == _parent682)) {
                var _old__min_ax12709 = _cursor707._min_ax12;
                var _old__min_ay13710 = _cursor707._min_ay13;
                var _old__max_ay24711 = _cursor707._max_ay24;
                var _old_height712 = _cursor707._height10;
                /* _min_ax12 is min of ax1 */
                var _augval713 = _cursor707.ax1;
                var _child714 = _cursor707._left7;
                if (!(_child714 == null)) {
                    var _val715 = _child714._min_ax12;
                    _augval713 = _augval713 < _val715 ? _augval713 : _val715;
                }
                var _child716 = _cursor707._right8;
                if (!(_child716 == null)) {
                    var _val717 = _child716._min_ax12;
                    _augval713 = _augval713 < _val717 ? _augval713 : _val717;
                }
                _cursor707._min_ax12 = _augval713;
                /* _min_ay13 is min of ay1 */
                var _augval718 = _cursor707.ay1;
                var _child719 = _cursor707._left7;
                if (!(_child719 == null)) {
                    var _val720 = _child719._min_ay13;
                    _augval718 = _augval718 < _val720 ? _augval718 : _val720;
                }
                var _child721 = _cursor707._right8;
                if (!(_child721 == null)) {
                    var _val722 = _child721._min_ay13;
                    _augval718 = _augval718 < _val722 ? _augval718 : _val722;
                }
                _cursor707._min_ay13 = _augval718;
                /* _max_ay24 is max of ay2 */
                var _augval723 = _cursor707.ay2;
                var _child724 = _cursor707._left7;
                if (!(_child724 == null)) {
                    var _val725 = _child724._max_ay24;
                    _augval723 = _augval723 < _val725 ? _val725 : _augval723;
                }
                var _child726 = _cursor707._right8;
                if (!(_child726 == null)) {
                    var _val727 = _child726._max_ay24;
                    _augval723 = _augval723 < _val727 ? _val727 : _augval723;
                }
                _cursor707._max_ay24 = _augval723;
                _cursor707._height10 = 1 + ((_cursor707._left7 == null ? -1 : _cursor707._left7._height10) > (
                        _cursor707._right8 == null ? -1 : _cursor707._right8._height10) ? _cursor707._left7 ==
                    null ? -1 : _cursor707._left7._height10 : _cursor707._right8 == null ? -1 : _cursor707
                    ._right8._height10);
                _changed708 = false;
                _changed708 = _changed708 || !(_old__min_ax12709 == _cursor707._min_ax12);
                _changed708 = _changed708 || !(_old__min_ay13710 == _cursor707._min_ay13);
                _changed708 = _changed708 || !(_old__max_ay24711 == _cursor707._max_ay24);
                _changed708 = _changed708 || !(_old_height712 == _cursor707._height10);
                _cursor707 = _cursor707._parent9;
            }
        }
        var _cursor728 = _parent682;
        var _changed729 = true;
        while (_changed729 && !(_cursor728 == null)) {
            var _old__min_ax12730 = _cursor728._min_ax12;
            var _old__min_ay13731 = _cursor728._min_ay13;
            var _old__max_ay24732 = _cursor728._max_ay24;
            var _old_height733 = _cursor728._height10;
            /* _min_ax12 is min of ax1 */
            var _augval734 = _cursor728.ax1;
            var _child735 = _cursor728._left7;
            if (!(_child735 == null)) {
                var _val736 = _child735._min_ax12;
                _augval734 = _augval734 < _val736 ? _augval734 : _val736;
            }
            var _child737 = _cursor728._right8;
            if (!(_child737 == null)) {
                var _val738 = _child737._min_ax12;
                _augval734 = _augval734 < _val738 ? _augval734 : _val738;
            }
            _cursor728._min_ax12 = _augval734;
            /* _min_ay13 is min of ay1 */
            var _augval739 = _cursor728.ay1;
            var _child740 = _cursor728._left7;
            if (!(_child740 == null)) {
                var _val741 = _child740._min_ay13;
                _augval739 = _augval739 < _val741 ? _augval739 : _val741;
            }
            var _child742 = _cursor728._right8;
            if (!(_child742 == null)) {
                var _val743 = _child742._min_ay13;
                _augval739 = _augval739 < _val743 ? _augval739 : _val743;
            }
            _cursor728._min_ay13 = _augval739;
            /* _max_ay24 is max of ay2 */
            var _augval744 = _cursor728.ay2;
            var _child745 = _cursor728._left7;
            if (!(_child745 == null)) {
                var _val746 = _child745._max_ay24;
                _augval744 = _augval744 < _val746 ? _val746 : _augval744;
            }
            var _child747 = _cursor728._right8;
            if (!(_child747 == null)) {
                var _val748 = _child747._max_ay24;
                _augval744 = _augval744 < _val748 ? _val748 : _augval744;
            }
            _cursor728._max_ay24 = _augval744;
            _cursor728._height10 = 1 + ((_cursor728._left7 == null ? -1 : _cursor728._left7._height10) > (_cursor728
                    ._right8 == null ? -1 : _cursor728._right8._height10) ? _cursor728._left7 == null ? -1 :
                _cursor728._left7._height10 : _cursor728._right8 == null ? -1 : _cursor728._right8._height10);
            _changed729 = false;
            _changed729 = _changed729 || !(_old__min_ax12730 == _cursor728._min_ax12);
            _changed729 = _changed729 || !(_old__min_ay13731 == _cursor728._min_ay13);
            _changed729 = _changed729 || !(_old__max_ay24732 == _cursor728._max_ay24);
            _changed729 = _changed729 || !(_old_height733 == _cursor728._height10);
            _cursor728 = _cursor728._parent9;
        }
        if (this._root1 == __x) {
            this._root1 = _new_x685;
        }
        __x._left7 = null;
        __x._right8 = null;
        __x._min_ax12 = __x.ax1;
        __x._min_ay13 = __x.ay1;
        __x._max_ay24 = __x.ay2;
        __x._height10 = 0;
        var _previous749 = null;
        var _current750 = this._root1;
        var _is_left751 = false;
        while (!(_current750 == null)) {
            _previous749 = _current750;
            if (ax2 < _current750.ax2) {
                _current750 = _current750._left7;
                _is_left751 = true;
            } else {
                _current750 = _current750._right8;
                _is_left751 = false;
            }
        }
        if (_previous749 == null) {
            this._root1 = __x;
        } else {
            __x._parent9 = _previous749;
            if (_is_left751) {
                _previous749._left7 = __x;
            } else {
                _previous749._right8 = __x;
            }
        }
        var _cursor752 = __x._parent9;
        var _changed753 = true;
        while (_changed753 && !(_cursor752 == null)) {
            var _old__min_ax12754 = _cursor752._min_ax12;
            var _old__min_ay13755 = _cursor752._min_ay13;
            var _old__max_ay24756 = _cursor752._max_ay24;
            var _old_height757 = _cursor752._height10;
            /* _min_ax12 is min of ax1 */
            var _augval758 = _cursor752.ax1;
            var _child759 = _cursor752._left7;
            if (!(_child759 == null)) {
                var _val760 = _child759._min_ax12;
                _augval758 = _augval758 < _val760 ? _augval758 : _val760;
            }
            var _child761 = _cursor752._right8;
            if (!(_child761 == null)) {
                var _val762 = _child761._min_ax12;
                _augval758 = _augval758 < _val762 ? _augval758 : _val762;
            }
            _cursor752._min_ax12 = _augval758;
            /* _min_ay13 is min of ay1 */
            var _augval763 = _cursor752.ay1;
            var _child764 = _cursor752._left7;
            if (!(_child764 == null)) {
                var _val765 = _child764._min_ay13;
                _augval763 = _augval763 < _val765 ? _augval763 : _val765;
            }
            var _child766 = _cursor752._right8;
            if (!(_child766 == null)) {
                var _val767 = _child766._min_ay13;
                _augval763 = _augval763 < _val767 ? _augval763 : _val767;
            }
            _cursor752._min_ay13 = _augval763;
            /* _max_ay24 is max of ay2 */
            var _augval768 = _cursor752.ay2;
            var _child769 = _cursor752._left7;
            if (!(_child769 == null)) {
                var _val770 = _child769._max_ay24;
                _augval768 = _augval768 < _val770 ? _val770 : _augval768;
            }
            var _child771 = _cursor752._right8;
            if (!(_child771 == null)) {
                var _val772 = _child771._max_ay24;
                _augval768 = _augval768 < _val772 ? _val772 : _augval768;
            }
            _cursor752._max_ay24 = _augval768;
            _cursor752._height10 = 1 + ((_cursor752._left7 == null ? -1 : _cursor752._left7._height10) > (_cursor752
                    ._right8 == null ? -1 : _cursor752._right8._height10) ? _cursor752._left7 == null ? -1 :
                _cursor752._left7._height10 : _cursor752._right8 == null ? -1 : _cursor752._right8._height10);
            _changed753 = false;
            _changed753 = _changed753 || !(_old__min_ax12754 == _cursor752._min_ax12);
            _changed753 = _changed753 || !(_old__min_ay13755 == _cursor752._min_ay13);
            _changed753 = _changed753 || !(_old__max_ay24756 == _cursor752._max_ay24);
            _changed753 = _changed753 || !(_old_height757 == _cursor752._height10);
            _cursor752 = _cursor752._parent9;
        }
        /* rebalance AVL tree */
        var _cursor773 = __x;
        var _imbalance774;
        while (!(_cursor773._parent9 == null)) {
            _cursor773 = _cursor773._parent9;
            _cursor773._height10 = 1 + ((_cursor773._left7 == null ? -1 : _cursor773._left7._height10) > (_cursor773
                    ._right8 == null ? -1 : _cursor773._right8._height10) ? _cursor773._left7 == null ? -1 :
                _cursor773._left7._height10 : _cursor773._right8 == null ? -1 : _cursor773._right8._height10);
            _imbalance774 = (_cursor773._left7 == null ? -1 : _cursor773._left7._height10) - (_cursor773._right8 ==
                null ? -1 : _cursor773._right8._height10);
            if (_imbalance774 > 1) {
                if (
                    (_cursor773._left7._left7 == null ? -1 : _cursor773._left7._left7._height10) < (_cursor773
                        ._left7._right8 == null ? -1 : _cursor773._left7._right8._height10)) {
                    /* rotate ((_cursor773)._left7)._right8 */
                    var _a775 = _cursor773._left7;
                    var _b776 = _a775._right8;
                    var _c777 = _b776._left7;
                    /* replace _a775 with _b776 in (_a775)._parent9 */
                    if (!(_a775._parent9 == null)) {
                        if (_a775._parent9._left7 == _a775) {
                            _a775._parent9._left7 = _b776;
                        } else {
                            _a775._parent9._right8 = _b776;
                        }
                    }
                    if (!(_b776 == null)) {
                        _b776._parent9 = _a775._parent9;
                    }
                    /* replace _c777 with _a775 in _b776 */
                    _b776._left7 = _a775;
                    if (!(_a775 == null)) {
                        _a775._parent9 = _b776;
                    }
                    /* replace _b776 with _c777 in _a775 */
                    _a775._right8 = _c777;
                    if (!(_c777 == null)) {
                        _c777._parent9 = _a775;
                    }
                    /* _min_ax12 is min of ax1 */
                    var _augval778 = _a775.ax1;
                    var _child779 = _a775._left7;
                    if (!(_child779 == null)) {
                        var _val780 = _child779._min_ax12;
                        _augval778 = _augval778 < _val780 ? _augval778 : _val780;
                    }
                    var _child781 = _a775._right8;
                    if (!(_child781 == null)) {
                        var _val782 = _child781._min_ax12;
                        _augval778 = _augval778 < _val782 ? _augval778 : _val782;
                    }
                    _a775._min_ax12 = _augval778;
                    /* _min_ay13 is min of ay1 */
                    var _augval783 = _a775.ay1;
                    var _child784 = _a775._left7;
                    if (!(_child784 == null)) {
                        var _val785 = _child784._min_ay13;
                        _augval783 = _augval783 < _val785 ? _augval783 : _val785;
                    }
                    var _child786 = _a775._right8;
                    if (!(_child786 == null)) {
                        var _val787 = _child786._min_ay13;
                        _augval783 = _augval783 < _val787 ? _augval783 : _val787;
                    }
                    _a775._min_ay13 = _augval783;
                    /* _max_ay24 is max of ay2 */
                    var _augval788 = _a775.ay2;
                    var _child789 = _a775._left7;
                    if (!(_child789 == null)) {
                        var _val790 = _child789._max_ay24;
                        _augval788 = _augval788 < _val790 ? _val790 : _augval788;
                    }
                    var _child791 = _a775._right8;
                    if (!(_child791 == null)) {
                        var _val792 = _child791._max_ay24;
                        _augval788 = _augval788 < _val792 ? _val792 : _augval788;
                    }
                    _a775._max_ay24 = _augval788;
                    _a775._height10 = 1 + ((_a775._left7 == null ? -1 : _a775._left7._height10) > (_a775._right8 ==
                            null ? -1 : _a775._right8._height10) ? _a775._left7 == null ? -1 : _a775._left7
                        ._height10 : _a775._right8 == null ? -1 : _a775._right8._height10);
                    /* _min_ax12 is min of ax1 */
                    var _augval793 = _b776.ax1;
                    var _child794 = _b776._left7;
                    if (!(_child794 == null)) {
                        var _val795 = _child794._min_ax12;
                        _augval793 = _augval793 < _val795 ? _augval793 : _val795;
                    }
                    var _child796 = _b776._right8;
                    if (!(_child796 == null)) {
                        var _val797 = _child796._min_ax12;
                        _augval793 = _augval793 < _val797 ? _augval793 : _val797;
                    }
                    _b776._min_ax12 = _augval793;
                    /* _min_ay13 is min of ay1 */
                    var _augval798 = _b776.ay1;
                    var _child799 = _b776._left7;
                    if (!(_child799 == null)) {
                        var _val800 = _child799._min_ay13;
                        _augval798 = _augval798 < _val800 ? _augval798 : _val800;
                    }
                    var _child801 = _b776._right8;
                    if (!(_child801 == null)) {
                        var _val802 = _child801._min_ay13;
                        _augval798 = _augval798 < _val802 ? _augval798 : _val802;
                    }
                    _b776._min_ay13 = _augval798;
                    /* _max_ay24 is max of ay2 */
                    var _augval803 = _b776.ay2;
                    var _child804 = _b776._left7;
                    if (!(_child804 == null)) {
                        var _val805 = _child804._max_ay24;
                        _augval803 = _augval803 < _val805 ? _val805 : _augval803;
                    }
                    var _child806 = _b776._right8;
                    if (!(_child806 == null)) {
                        var _val807 = _child806._max_ay24;
                        _augval803 = _augval803 < _val807 ? _val807 : _augval803;
                    }
                    _b776._max_ay24 = _augval803;
                    _b776._height10 = 1 + ((_b776._left7 == null ? -1 : _b776._left7._height10) > (_b776._right8 ==
                            null ? -1 : _b776._right8._height10) ? _b776._left7 == null ? -1 : _b776._left7
                        ._height10 : _b776._right8 == null ? -1 : _b776._right8._height10);
                    if (!(_b776._parent9 == null)) {
                        /* _min_ax12 is min of ax1 */
                        var _augval808 = _b776._parent9.ax1;
                        var _child809 = _b776._parent9._left7;
                        if (!(_child809 == null)) {
                            var _val810 = _child809._min_ax12;
                            _augval808 = _augval808 < _val810 ? _augval808 : _val810;
                        }
                        var _child811 = _b776._parent9._right8;
                        if (!(_child811 == null)) {
                            var _val812 = _child811._min_ax12;
                            _augval808 = _augval808 < _val812 ? _augval808 : _val812;
                        }
                        _b776._parent9._min_ax12 = _augval808;
                        /* _min_ay13 is min of ay1 */
                        var _augval813 = _b776._parent9.ay1;
                        var _child814 = _b776._parent9._left7;
                        if (!(_child814 == null)) {
                            var _val815 = _child814._min_ay13;
                            _augval813 = _augval813 < _val815 ? _augval813 : _val815;
                        }
                        var _child816 = _b776._parent9._right8;
                        if (!(_child816 == null)) {
                            var _val817 = _child816._min_ay13;
                            _augval813 = _augval813 < _val817 ? _augval813 : _val817;
                        }
                        _b776._parent9._min_ay13 = _augval813;
                        /* _max_ay24 is max of ay2 */
                        var _augval818 = _b776._parent9.ay2;
                        var _child819 = _b776._parent9._left7;
                        if (!(_child819 == null)) {
                            var _val820 = _child819._max_ay24;
                            _augval818 = _augval818 < _val820 ? _val820 : _augval818;
                        }
                        var _child821 = _b776._parent9._right8;
                        if (!(_child821 == null)) {
                            var _val822 = _child821._max_ay24;
                            _augval818 = _augval818 < _val822 ? _val822 : _augval818;
                        }
                        _b776._parent9._max_ay24 = _augval818;
                        _b776._parent9._height10 = 1 + ((_b776._parent9._left7 == null ? -1 : _b776._parent9._left7
                                ._height10) > (_b776._parent9._right8 == null ? -1 : _b776._parent9._right8
                                ._height10) ? _b776._parent9._left7 == null ? -1 : _b776._parent9._left7
                            ._height10 : _b776._parent9._right8 == null ? -1 : _b776._parent9._right8._height10);
                    } else {
                        this._root1 = _b776;
                    }
                }
                /* rotate (_cursor773)._left7 */
                var _a823 = _cursor773;
                var _b824 = _a823._left7;
                var _c825 = _b824._right8;
                /* replace _a823 with _b824 in (_a823)._parent9 */
                if (!(_a823._parent9 == null)) {
                    if (_a823._parent9._left7 == _a823) {
                        _a823._parent9._left7 = _b824;
                    } else {
                        _a823._parent9._right8 = _b824;
                    }
                }
                if (!(_b824 == null)) {
                    _b824._parent9 = _a823._parent9;
                }
                /* replace _c825 with _a823 in _b824 */
                _b824._right8 = _a823;
                if (!(_a823 == null)) {
                    _a823._parent9 = _b824;
                }
                /* replace _b824 with _c825 in _a823 */
                _a823._left7 = _c825;
                if (!(_c825 == null)) {
                    _c825._parent9 = _a823;
                }
                /* _min_ax12 is min of ax1 */
                var _augval826 = _a823.ax1;
                var _child827 = _a823._left7;
                if (!(_child827 == null)) {
                    var _val828 = _child827._min_ax12;
                    _augval826 = _augval826 < _val828 ? _augval826 : _val828;
                }
                var _child829 = _a823._right8;
                if (!(_child829 == null)) {
                    var _val830 = _child829._min_ax12;
                    _augval826 = _augval826 < _val830 ? _augval826 : _val830;
                }
                _a823._min_ax12 = _augval826;
                /* _min_ay13 is min of ay1 */
                var _augval831 = _a823.ay1;
                var _child832 = _a823._left7;
                if (!(_child832 == null)) {
                    var _val833 = _child832._min_ay13;
                    _augval831 = _augval831 < _val833 ? _augval831 : _val833;
                }
                var _child834 = _a823._right8;
                if (!(_child834 == null)) {
                    var _val835 = _child834._min_ay13;
                    _augval831 = _augval831 < _val835 ? _augval831 : _val835;
                }
                _a823._min_ay13 = _augval831;
                /* _max_ay24 is max of ay2 */
                var _augval836 = _a823.ay2;
                var _child837 = _a823._left7;
                if (!(_child837 == null)) {
                    var _val838 = _child837._max_ay24;
                    _augval836 = _augval836 < _val838 ? _val838 : _augval836;
                }
                var _child839 = _a823._right8;
                if (!(_child839 == null)) {
                    var _val840 = _child839._max_ay24;
                    _augval836 = _augval836 < _val840 ? _val840 : _augval836;
                }
                _a823._max_ay24 = _augval836;
                _a823._height10 = 1 + ((_a823._left7 == null ? -1 : _a823._left7._height10) > (_a823._right8 ==
                        null ? -1 : _a823._right8._height10) ? _a823._left7 == null ? -1 : _a823._left7
                    ._height10 : _a823._right8 == null ? -1 : _a823._right8._height10);
                /* _min_ax12 is min of ax1 */
                var _augval841 = _b824.ax1;
                var _child842 = _b824._left7;
                if (!(_child842 == null)) {
                    var _val843 = _child842._min_ax12;
                    _augval841 = _augval841 < _val843 ? _augval841 : _val843;
                }
                var _child844 = _b824._right8;
                if (!(_child844 == null)) {
                    var _val845 = _child844._min_ax12;
                    _augval841 = _augval841 < _val845 ? _augval841 : _val845;
                }
                _b824._min_ax12 = _augval841;
                /* _min_ay13 is min of ay1 */
                var _augval846 = _b824.ay1;
                var _child847 = _b824._left7;
                if (!(_child847 == null)) {
                    var _val848 = _child847._min_ay13;
                    _augval846 = _augval846 < _val848 ? _augval846 : _val848;
                }
                var _child849 = _b824._right8;
                if (!(_child849 == null)) {
                    var _val850 = _child849._min_ay13;
                    _augval846 = _augval846 < _val850 ? _augval846 : _val850;
                }
                _b824._min_ay13 = _augval846;
                /* _max_ay24 is max of ay2 */
                var _augval851 = _b824.ay2;
                var _child852 = _b824._left7;
                if (!(_child852 == null)) {
                    var _val853 = _child852._max_ay24;
                    _augval851 = _augval851 < _val853 ? _val853 : _augval851;
                }
                var _child854 = _b824._right8;
                if (!(_child854 == null)) {
                    var _val855 = _child854._max_ay24;
                    _augval851 = _augval851 < _val855 ? _val855 : _augval851;
                }
                _b824._max_ay24 = _augval851;
                _b824._height10 = 1 + ((_b824._left7 == null ? -1 : _b824._left7._height10) > (_b824._right8 ==
                        null ? -1 : _b824._right8._height10) ? _b824._left7 == null ? -1 : _b824._left7
                    ._height10 : _b824._right8 == null ? -1 : _b824._right8._height10);
                if (!(_b824._parent9 == null)) {
                    /* _min_ax12 is min of ax1 */
                    var _augval856 = _b824._parent9.ax1;
                    var _child857 = _b824._parent9._left7;
                    if (!(_child857 == null)) {
                        var _val858 = _child857._min_ax12;
                        _augval856 = _augval856 < _val858 ? _augval856 : _val858;
                    }
                    var _child859 = _b824._parent9._right8;
                    if (!(_child859 == null)) {
                        var _val860 = _child859._min_ax12;
                        _augval856 = _augval856 < _val860 ? _augval856 : _val860;
                    }
                    _b824._parent9._min_ax12 = _augval856;
                    /* _min_ay13 is min of ay1 */
                    var _augval861 = _b824._parent9.ay1;
                    var _child862 = _b824._parent9._left7;
                    if (!(_child862 == null)) {
                        var _val863 = _child862._min_ay13;
                        _augval861 = _augval861 < _val863 ? _augval861 : _val863;
                    }
                    var _child864 = _b824._parent9._right8;
                    if (!(_child864 == null)) {
                        var _val865 = _child864._min_ay13;
                        _augval861 = _augval861 < _val865 ? _augval861 : _val865;
                    }
                    _b824._parent9._min_ay13 = _augval861;
                    /* _max_ay24 is max of ay2 */
                    var _augval866 = _b824._parent9.ay2;
                    var _child867 = _b824._parent9._left7;
                    if (!(_child867 == null)) {
                        var _val868 = _child867._max_ay24;
                        _augval866 = _augval866 < _val868 ? _val868 : _augval866;
                    }
                    var _child869 = _b824._parent9._right8;
                    if (!(_child869 == null)) {
                        var _val870 = _child869._max_ay24;
                        _augval866 = _augval866 < _val870 ? _val870 : _augval866;
                    }
                    _b824._parent9._max_ay24 = _augval866;
                    _b824._parent9._height10 = 1 + ((_b824._parent9._left7 == null ? -1 : _b824._parent9._left7
                            ._height10) > (_b824._parent9._right8 == null ? -1 : _b824._parent9._right8
                            ._height10) ? _b824._parent9._left7 == null ? -1 : _b824._parent9._left7._height10 :
                        _b824._parent9._right8 == null ? -1 : _b824._parent9._right8._height10);
                } else {
                    this._root1 = _b824;
                }
                _cursor773 = _cursor773._parent9;
            } else if (_imbalance774 < -1) {
                if (
                    (_cursor773._right8._left7 == null ? -1 : _cursor773._right8._left7._height10) > (_cursor773
                        ._right8._right8 == null ? -1 : _cursor773._right8._right8._height10)) {
                    /* rotate ((_cursor773)._right8)._left7 */
                    var _a871 = _cursor773._right8;
                    var _b872 = _a871._left7;
                    var _c873 = _b872._right8;
                    /* replace _a871 with _b872 in (_a871)._parent9 */
                    if (!(_a871._parent9 == null)) {
                        if (_a871._parent9._left7 == _a871) {
                            _a871._parent9._left7 = _b872;
                        } else {
                            _a871._parent9._right8 = _b872;
                        }
                    }
                    if (!(_b872 == null)) {
                        _b872._parent9 = _a871._parent9;
                    }
                    /* replace _c873 with _a871 in _b872 */
                    _b872._right8 = _a871;
                    if (!(_a871 == null)) {
                        _a871._parent9 = _b872;
                    }
                    /* replace _b872 with _c873 in _a871 */
                    _a871._left7 = _c873;
                    if (!(_c873 == null)) {
                        _c873._parent9 = _a871;
                    }
                    /* _min_ax12 is min of ax1 */
                    var _augval874 = _a871.ax1;
                    var _child875 = _a871._left7;
                    if (!(_child875 == null)) {
                        var _val876 = _child875._min_ax12;
                        _augval874 = _augval874 < _val876 ? _augval874 : _val876;
                    }
                    var _child877 = _a871._right8;
                    if (!(_child877 == null)) {
                        var _val878 = _child877._min_ax12;
                        _augval874 = _augval874 < _val878 ? _augval874 : _val878;
                    }
                    _a871._min_ax12 = _augval874;
                    /* _min_ay13 is min of ay1 */
                    var _augval879 = _a871.ay1;
                    var _child880 = _a871._left7;
                    if (!(_child880 == null)) {
                        var _val881 = _child880._min_ay13;
                        _augval879 = _augval879 < _val881 ? _augval879 : _val881;
                    }
                    var _child882 = _a871._right8;
                    if (!(_child882 == null)) {
                        var _val883 = _child882._min_ay13;
                        _augval879 = _augval879 < _val883 ? _augval879 : _val883;
                    }
                    _a871._min_ay13 = _augval879;
                    /* _max_ay24 is max of ay2 */
                    var _augval884 = _a871.ay2;
                    var _child885 = _a871._left7;
                    if (!(_child885 == null)) {
                        var _val886 = _child885._max_ay24;
                        _augval884 = _augval884 < _val886 ? _val886 : _augval884;
                    }
                    var _child887 = _a871._right8;
                    if (!(_child887 == null)) {
                        var _val888 = _child887._max_ay24;
                        _augval884 = _augval884 < _val888 ? _val888 : _augval884;
                    }
                    _a871._max_ay24 = _augval884;
                    _a871._height10 = 1 + ((_a871._left7 == null ? -1 : _a871._left7._height10) > (_a871._right8 ==
                            null ? -1 : _a871._right8._height10) ? _a871._left7 == null ? -1 : _a871._left7
                        ._height10 : _a871._right8 == null ? -1 : _a871._right8._height10);
                    /* _min_ax12 is min of ax1 */
                    var _augval889 = _b872.ax1;
                    var _child890 = _b872._left7;
                    if (!(_child890 == null)) {
                        var _val891 = _child890._min_ax12;
                        _augval889 = _augval889 < _val891 ? _augval889 : _val891;
                    }
                    var _child892 = _b872._right8;
                    if (!(_child892 == null)) {
                        var _val893 = _child892._min_ax12;
                        _augval889 = _augval889 < _val893 ? _augval889 : _val893;
                    }
                    _b872._min_ax12 = _augval889;
                    /* _min_ay13 is min of ay1 */
                    var _augval894 = _b872.ay1;
                    var _child895 = _b872._left7;
                    if (!(_child895 == null)) {
                        var _val896 = _child895._min_ay13;
                        _augval894 = _augval894 < _val896 ? _augval894 : _val896;
                    }
                    var _child897 = _b872._right8;
                    if (!(_child897 == null)) {
                        var _val898 = _child897._min_ay13;
                        _augval894 = _augval894 < _val898 ? _augval894 : _val898;
                    }
                    _b872._min_ay13 = _augval894;
                    /* _max_ay24 is max of ay2 */
                    var _augval899 = _b872.ay2;
                    var _child900 = _b872._left7;
                    if (!(_child900 == null)) {
                        var _val901 = _child900._max_ay24;
                        _augval899 = _augval899 < _val901 ? _val901 : _augval899;
                    }
                    var _child902 = _b872._right8;
                    if (!(_child902 == null)) {
                        var _val903 = _child902._max_ay24;
                        _augval899 = _augval899 < _val903 ? _val903 : _augval899;
                    }
                    _b872._max_ay24 = _augval899;
                    _b872._height10 = 1 + ((_b872._left7 == null ? -1 : _b872._left7._height10) > (_b872._right8 ==
                            null ? -1 : _b872._right8._height10) ? _b872._left7 == null ? -1 : _b872._left7
                        ._height10 : _b872._right8 == null ? -1 : _b872._right8._height10);
                    if (!(_b872._parent9 == null)) {
                        /* _min_ax12 is min of ax1 */
                        var _augval904 = _b872._parent9.ax1;
                        var _child905 = _b872._parent9._left7;
                        if (!(_child905 == null)) {
                            var _val906 = _child905._min_ax12;
                            _augval904 = _augval904 < _val906 ? _augval904 : _val906;
                        }
                        var _child907 = _b872._parent9._right8;
                        if (!(_child907 == null)) {
                            var _val908 = _child907._min_ax12;
                            _augval904 = _augval904 < _val908 ? _augval904 : _val908;
                        }
                        _b872._parent9._min_ax12 = _augval904;
                        /* _min_ay13 is min of ay1 */
                        var _augval909 = _b872._parent9.ay1;
                        var _child910 = _b872._parent9._left7;
                        if (!(_child910 == null)) {
                            var _val911 = _child910._min_ay13;
                            _augval909 = _augval909 < _val911 ? _augval909 : _val911;
                        }
                        var _child912 = _b872._parent9._right8;
                        if (!(_child912 == null)) {
                            var _val913 = _child912._min_ay13;
                            _augval909 = _augval909 < _val913 ? _augval909 : _val913;
                        }
                        _b872._parent9._min_ay13 = _augval909;
                        /* _max_ay24 is max of ay2 */
                        var _augval914 = _b872._parent9.ay2;
                        var _child915 = _b872._parent9._left7;
                        if (!(_child915 == null)) {
                            var _val916 = _child915._max_ay24;
                            _augval914 = _augval914 < _val916 ? _val916 : _augval914;
                        }
                        var _child917 = _b872._parent9._right8;
                        if (!(_child917 == null)) {
                            var _val918 = _child917._max_ay24;
                            _augval914 = _augval914 < _val918 ? _val918 : _augval914;
                        }
                        _b872._parent9._max_ay24 = _augval914;
                        _b872._parent9._height10 = 1 + ((_b872._parent9._left7 == null ? -1 : _b872._parent9._left7
                                ._height10) > (_b872._parent9._right8 == null ? -1 : _b872._parent9._right8
                                ._height10) ? _b872._parent9._left7 == null ? -1 : _b872._parent9._left7
                            ._height10 : _b872._parent9._right8 == null ? -1 : _b872._parent9._right8._height10);
                    } else {
                        this._root1 = _b872;
                    }
                }
                /* rotate (_cursor773)._right8 */
                var _a919 = _cursor773;
                var _b920 = _a919._right8;
                var _c921 = _b920._left7;
                /* replace _a919 with _b920 in (_a919)._parent9 */
                if (!(_a919._parent9 == null)) {
                    if (_a919._parent9._left7 == _a919) {
                        _a919._parent9._left7 = _b920;
                    } else {
                        _a919._parent9._right8 = _b920;
                    }
                }
                if (!(_b920 == null)) {
                    _b920._parent9 = _a919._parent9;
                }
                /* replace _c921 with _a919 in _b920 */
                _b920._left7 = _a919;
                if (!(_a919 == null)) {
                    _a919._parent9 = _b920;
                }
                /* replace _b920 with _c921 in _a919 */
                _a919._right8 = _c921;
                if (!(_c921 == null)) {
                    _c921._parent9 = _a919;
                }
                /* _min_ax12 is min of ax1 */
                var _augval922 = _a919.ax1;
                var _child923 = _a919._left7;
                if (!(_child923 == null)) {
                    var _val924 = _child923._min_ax12;
                    _augval922 = _augval922 < _val924 ? _augval922 : _val924;
                }
                var _child925 = _a919._right8;
                if (!(_child925 == null)) {
                    var _val926 = _child925._min_ax12;
                    _augval922 = _augval922 < _val926 ? _augval922 : _val926;
                }
                _a919._min_ax12 = _augval922;
                /* _min_ay13 is min of ay1 */
                var _augval927 = _a919.ay1;
                var _child928 = _a919._left7;
                if (!(_child928 == null)) {
                    var _val929 = _child928._min_ay13;
                    _augval927 = _augval927 < _val929 ? _augval927 : _val929;
                }
                var _child930 = _a919._right8;
                if (!(_child930 == null)) {
                    var _val931 = _child930._min_ay13;
                    _augval927 = _augval927 < _val931 ? _augval927 : _val931;
                }
                _a919._min_ay13 = _augval927;
                /* _max_ay24 is max of ay2 */
                var _augval932 = _a919.ay2;
                var _child933 = _a919._left7;
                if (!(_child933 == null)) {
                    var _val934 = _child933._max_ay24;
                    _augval932 = _augval932 < _val934 ? _val934 : _augval932;
                }
                var _child935 = _a919._right8;
                if (!(_child935 == null)) {
                    var _val936 = _child935._max_ay24;
                    _augval932 = _augval932 < _val936 ? _val936 : _augval932;
                }
                _a919._max_ay24 = _augval932;
                _a919._height10 = 1 + ((_a919._left7 == null ? -1 : _a919._left7._height10) > (_a919._right8 ==
                        null ? -1 : _a919._right8._height10) ? _a919._left7 == null ? -1 : _a919._left7
                    ._height10 : _a919._right8 == null ? -1 : _a919._right8._height10);
                /* _min_ax12 is min of ax1 */
                var _augval937 = _b920.ax1;
                var _child938 = _b920._left7;
                if (!(_child938 == null)) {
                    var _val939 = _child938._min_ax12;
                    _augval937 = _augval937 < _val939 ? _augval937 : _val939;
                }
                var _child940 = _b920._right8;
                if (!(_child940 == null)) {
                    var _val941 = _child940._min_ax12;
                    _augval937 = _augval937 < _val941 ? _augval937 : _val941;
                }
                _b920._min_ax12 = _augval937;
                /* _min_ay13 is min of ay1 */
                var _augval942 = _b920.ay1;
                var _child943 = _b920._left7;
                if (!(_child943 == null)) {
                    var _val944 = _child943._min_ay13;
                    _augval942 = _augval942 < _val944 ? _augval942 : _val944;
                }
                var _child945 = _b920._right8;
                if (!(_child945 == null)) {
                    var _val946 = _child945._min_ay13;
                    _augval942 = _augval942 < _val946 ? _augval942 : _val946;
                }
                _b920._min_ay13 = _augval942;
                /* _max_ay24 is max of ay2 */
                var _augval947 = _b920.ay2;
                var _child948 = _b920._left7;
                if (!(_child948 == null)) {
                    var _val949 = _child948._max_ay24;
                    _augval947 = _augval947 < _val949 ? _val949 : _augval947;
                }
                var _child950 = _b920._right8;
                if (!(_child950 == null)) {
                    var _val951 = _child950._max_ay24;
                    _augval947 = _augval947 < _val951 ? _val951 : _augval947;
                }
                _b920._max_ay24 = _augval947;
                _b920._height10 = 1 + ((_b920._left7 == null ? -1 : _b920._left7._height10) > (_b920._right8 ==
                        null ? -1 : _b920._right8._height10) ? _b920._left7 == null ? -1 : _b920._left7
                    ._height10 : _b920._right8 == null ? -1 : _b920._right8._height10);
                if (!(_b920._parent9 == null)) {
                    /* _min_ax12 is min of ax1 */
                    var _augval952 = _b920._parent9.ax1;
                    var _child953 = _b920._parent9._left7;
                    if (!(_child953 == null)) {
                        var _val954 = _child953._min_ax12;
                        _augval952 = _augval952 < _val954 ? _augval952 : _val954;
                    }
                    var _child955 = _b920._parent9._right8;
                    if (!(_child955 == null)) {
                        var _val956 = _child955._min_ax12;
                        _augval952 = _augval952 < _val956 ? _augval952 : _val956;
                    }
                    _b920._parent9._min_ax12 = _augval952;
                    /* _min_ay13 is min of ay1 */
                    var _augval957 = _b920._parent9.ay1;
                    var _child958 = _b920._parent9._left7;
                    if (!(_child958 == null)) {
                        var _val959 = _child958._min_ay13;
                        _augval957 = _augval957 < _val959 ? _augval957 : _val959;
                    }
                    var _child960 = _b920._parent9._right8;
                    if (!(_child960 == null)) {
                        var _val961 = _child960._min_ay13;
                        _augval957 = _augval957 < _val961 ? _augval957 : _val961;
                    }
                    _b920._parent9._min_ay13 = _augval957;
                    /* _max_ay24 is max of ay2 */
                    var _augval962 = _b920._parent9.ay2;
                    var _child963 = _b920._parent9._left7;
                    if (!(_child963 == null)) {
                        var _val964 = _child963._max_ay24;
                        _augval962 = _augval962 < _val964 ? _val964 : _augval962;
                    }
                    var _child965 = _b920._parent9._right8;
                    if (!(_child965 == null)) {
                        var _val966 = _child965._max_ay24;
                        _augval962 = _augval962 < _val966 ? _val966 : _augval962;
                    }
                    _b920._parent9._max_ay24 = _augval962;
                    _b920._parent9._height10 = 1 + ((_b920._parent9._left7 == null ? -1 : _b920._parent9._left7
                            ._height10) > (_b920._parent9._right8 == null ? -1 : _b920._parent9._right8
                            ._height10) ? _b920._parent9._left7 == null ? -1 : _b920._parent9._left7._height10 :
                        _b920._parent9._right8 == null ? -1 : _b920._parent9._right8._height10);
                } else {
                    this._root1 = _b920;
                }
                _cursor773 = _cursor773._parent9;
            }
        }
        __x.ax1 = ax1;
        __x.ay1 = ay1;
        __x.ax2 = ax2;
        __x.ay2 = ay2;
    };
    RectangleHolder.prototype.findMatchingRectangles = function (bx1, by1, bx2, by2, __callback) {
        var _root967 = this._root1;
        var _x968 = _root967;
        var _descend969 = true;
        var _from_left970 = true;
        while (true) {
            if (_x968 == null) {
                _x968 = null;
                break;
            }
            if (_descend969) {
                /* too small? */
                if (false || _x968.ax2 <= bx1) {
                    if (!(_x968._right8 == null) && true && _x968._right8._min_ax12 < bx2 && _x968._right8
                        ._min_ay13 < by2 && _x968._right8._max_ay24 > by1) {
                        if (_x968 == _root967) {
                            _root967 = _x968._right8;
                        }
                        _x968 = _x968._right8;
                    } else if (_x968 == _root967) {
                        _x968 = null;
                        break;
                    } else {
                        _descend969 = false;
                        _from_left970 = !(_x968._parent9 == null) && _x968 == _x968._parent9._left7;
                        _x968 = _x968._parent9;
                    }
                } else if (!(_x968._left7 == null) && true && _x968._left7._min_ax12 < bx2 && _x968._left7
                    ._min_ay13 < by2 && _x968._left7._max_ay24 > by1) {
                    _x968 = _x968._left7;
                    /* too large? */
                } else if (false) {
                    if (_x968 == _root967) {
                        _x968 = null;
                        break;
                    } else {
                        _descend969 = false;
                        _from_left970 = !(_x968._parent9 == null) && _x968 == _x968._parent9._left7;
                        _x968 = _x968._parent9;
                    }
                    /* node ok? */
                } else if (true && _x968.ax1 < bx2 && _x968.ay1 < by2 && _x968.ay2 > by1) {
                    break;
                } else if (_x968 == _root967) {
                    _root967 = _x968._right8;
                    _x968 = _x968._right8;
                } else {
                    if (!(_x968._right8 == null) && true && _x968._right8._min_ax12 < bx2 && _x968._right8
                        ._min_ay13 < by2 && _x968._right8._max_ay24 > by1) {
                        if (_x968 == _root967) {
                            _root967 = _x968._right8;
                        }
                        _x968 = _x968._right8;
                    } else {
                        _descend969 = false;
                        _from_left970 = !(_x968._parent9 == null) && _x968 == _x968._parent9._left7;
                        _x968 = _x968._parent9;
                    }
                }
            } else if (_from_left970) {
                if (false) {
                    _x968 = null;
                    break;
                } else if (true && _x968.ax1 < bx2 && _x968.ay1 < by2 && _x968.ay2 > by1) {
                    break;
                } else if (!(_x968._right8 == null) && true && _x968._right8._min_ax12 < bx2 && _x968._right8
                    ._min_ay13 < by2 && _x968._right8._max_ay24 > by1) {
                    _descend969 = true;
                    if (_x968 == _root967) {
                        _root967 = _x968._right8;
                    }
                    _x968 = _x968._right8;
                } else if (_x968 == _root967) {
                    _x968 = null;
                    break;
                } else {
                    _descend969 = false;
                    _from_left970 = !(_x968._parent9 == null) && _x968 == _x968._parent9._left7;
                    _x968 = _x968._parent9;
                }
            } else {
                if (_x968 == _root967) {
                    _x968 = null;
                    break;
                } else {
                    _descend969 = false;
                    _from_left970 = !(_x968._parent9 == null) && _x968 == _x968._parent9._left7;
                    _x968 = _x968._parent9;
                }
            }
        }
        var _prev_cursor5 = null;
        var _cursor6 = _x968;
        for (;;) {
            if (!!(_cursor6 == null)) break;
            var _name971 = _cursor6;
            /* ADVANCE */
            _prev_cursor5 = _cursor6;
            do {
                var _right_min972 = null;
                if (!(_cursor6._right8 == null) && true && _cursor6._right8._min_ax12 < bx2 && _cursor6._right8
                    ._min_ay13 < by2 && _cursor6._right8._max_ay24 > by1) {
                    var _root973 = _cursor6._right8;
                    var _x974 = _root973;
                    var _descend975 = true;
                    var _from_left976 = true;
                    while (true) {
                        if (_x974 == null) {
                            _x974 = null;
                            break;
                        }
                        if (_descend975) {
                            /* too small? */
                            if (false || _x974.ax2 <= bx1) {
                                if (!(_x974._right8 == null) && true && _x974._right8._min_ax12 < bx2 && _x974
                                    ._right8._min_ay13 < by2 && _x974._right8._max_ay24 > by1) {
                                    if (_x974 == _root973) {
                                        _root973 = _x974._right8;
                                    }
                                    _x974 = _x974._right8;
                                } else if (_x974 == _root973) {
                                    _x974 = null;
                                    break;
                                } else {
                                    _descend975 = false;
                                    _from_left976 = !(_x974._parent9 == null) && _x974 == _x974._parent9._left7;
                                    _x974 = _x974._parent9;
                                }
                            } else if (!(_x974._left7 == null) && true && _x974._left7._min_ax12 < bx2 && _x974
                                ._left7._min_ay13 < by2 && _x974._left7._max_ay24 > by1) {
                                _x974 = _x974._left7;
                                /* too large? */
                            } else if (false) {
                                if (_x974 == _root973) {
                                    _x974 = null;
                                    break;
                                } else {
                                    _descend975 = false;
                                    _from_left976 = !(_x974._parent9 == null) && _x974 == _x974._parent9._left7;
                                    _x974 = _x974._parent9;
                                }
                                /* node ok? */
                            } else if (true && _x974.ax1 < bx2 && _x974.ay1 < by2 && _x974.ay2 > by1) {
                                break;
                            } else if (_x974 == _root973) {
                                _root973 = _x974._right8;
                                _x974 = _x974._right8;
                            } else {
                                if (!(_x974._right8 == null) && true && _x974._right8._min_ax12 < bx2 && _x974
                                    ._right8._min_ay13 < by2 && _x974._right8._max_ay24 > by1) {
                                    if (_x974 == _root973) {
                                        _root973 = _x974._right8;
                                    }
                                    _x974 = _x974._right8;
                                } else {
                                    _descend975 = false;
                                    _from_left976 = !(_x974._parent9 == null) && _x974 == _x974._parent9._left7;
                                    _x974 = _x974._parent9;
                                }
                            }
                        } else if (_from_left976) {
                            if (false) {
                                _x974 = null;
                                break;
                            } else if (true && _x974.ax1 < bx2 && _x974.ay1 < by2 && _x974.ay2 > by1) {
                                break;
                            } else if (!(_x974._right8 == null) && true && _x974._right8._min_ax12 < bx2 && _x974
                                ._right8._min_ay13 < by2 && _x974._right8._max_ay24 > by1) {
                                _descend975 = true;
                                if (_x974 == _root973) {
                                    _root973 = _x974._right8;
                                }
                                _x974 = _x974._right8;
                            } else if (_x974 == _root973) {
                                _x974 = null;
                                break;
                            } else {
                                _descend975 = false;
                                _from_left976 = !(_x974._parent9 == null) && _x974 == _x974._parent9._left7;
                                _x974 = _x974._parent9;
                            }
                        } else {
                            if (_x974 == _root973) {
                                _x974 = null;
                                break;
                            } else {
                                _descend975 = false;
                                _from_left976 = !(_x974._parent9 == null) && _x974 == _x974._parent9._left7;
                                _x974 = _x974._parent9;
                            }
                        }
                    }
                    _right_min972 = _x974;
                }
                if (!(_right_min972 == null)) {
                    _cursor6 = _right_min972;
                    break;
                } else {
                    while (!(_cursor6._parent9 == null) && _cursor6 == _cursor6._parent9._right8) {
                        _cursor6 = _cursor6._parent9;
                    }
                    _cursor6 = _cursor6._parent9;
                    if (!(_cursor6 == null) && false) {
                        _cursor6 = null;
                    }
                }
            } while (!(_cursor6 == null) && !(true && _cursor6.ax1 < bx2 && _cursor6.ay1 < by2 && _cursor6.ay2 >
                    by1));
            if (__callback(_name971)) {
                var _to_remove977 = _prev_cursor5;
                var _parent978 = _to_remove977._parent9;
                var _left979 = _to_remove977._left7;
                var _right980 = _to_remove977._right8;
                var _new_x981;
                if (_left979 == null && _right980 == null) {
                    _new_x981 = null;
                    /* replace _to_remove977 with _new_x981 in _parent978 */
                    if (!(_parent978 == null)) {
                        if (_parent978._left7 == _to_remove977) {
                            _parent978._left7 = _new_x981;
                        } else {
                            _parent978._right8 = _new_x981;
                        }
                    }
                    if (!(_new_x981 == null)) {
                        _new_x981._parent9 = _parent978;
                    }
                } else if (!(_left979 == null) && _right980 == null) {
                    _new_x981 = _left979;
                    /* replace _to_remove977 with _new_x981 in _parent978 */
                    if (!(_parent978 == null)) {
                        if (_parent978._left7 == _to_remove977) {
                            _parent978._left7 = _new_x981;
                        } else {
                            _parent978._right8 = _new_x981;
                        }
                    }
                    if (!(_new_x981 == null)) {
                        _new_x981._parent9 = _parent978;
                    }
                } else if (_left979 == null && !(_right980 == null)) {
                    _new_x981 = _right980;
                    /* replace _to_remove977 with _new_x981 in _parent978 */
                    if (!(_parent978 == null)) {
                        if (_parent978._left7 == _to_remove977) {
                            _parent978._left7 = _new_x981;
                        } else {
                            _parent978._right8 = _new_x981;
                        }
                    }
                    if (!(_new_x981 == null)) {
                        _new_x981._parent9 = _parent978;
                    }
                } else {
                    var _root982 = _to_remove977._right8;
                    var _x983 = _root982;
                    var _descend984 = true;
                    var _from_left985 = true;
                    while (true) {
                        if (_x983 == null) {
                            _x983 = null;
                            break;
                        }
                        if (_descend984) {
                            /* too small? */
                            if (false) {
                                if (!(_x983._right8 == null) && true) {
                                    if (_x983 == _root982) {
                                        _root982 = _x983._right8;
                                    }
                                    _x983 = _x983._right8;
                                } else if (_x983 == _root982) {
                                    _x983 = null;
                                    break;
                                } else {
                                    _descend984 = false;
                                    _from_left985 = !(_x983._parent9 == null) && _x983 == _x983._parent9._left7;
                                    _x983 = _x983._parent9;
                                }
                            } else if (!(_x983._left7 == null) && true) {
                                _x983 = _x983._left7;
                                /* too large? */
                            } else if (false) {
                                if (_x983 == _root982) {
                                    _x983 = null;
                                    break;
                                } else {
                                    _descend984 = false;
                                    _from_left985 = !(_x983._parent9 == null) && _x983 == _x983._parent9._left7;
                                    _x983 = _x983._parent9;
                                }
                                /* node ok? */
                            } else if (true) {
                                break;
                            } else if (_x983 == _root982) {
                                _root982 = _x983._right8;
                                _x983 = _x983._right8;
                            } else {
                                if (!(_x983._right8 == null) && true) {
                                    if (_x983 == _root982) {
                                        _root982 = _x983._right8;
                                    }
                                    _x983 = _x983._right8;
                                } else {
                                    _descend984 = false;
                                    _from_left985 = !(_x983._parent9 == null) && _x983 == _x983._parent9._left7;
                                    _x983 = _x983._parent9;
                                }
                            }
                        } else if (_from_left985) {
                            if (false) {
                                _x983 = null;
                                break;
                            } else if (true) {
                                break;
                            } else if (!(_x983._right8 == null) && true) {
                                _descend984 = true;
                                if (_x983 == _root982) {
                                    _root982 = _x983._right8;
                                }
                                _x983 = _x983._right8;
                            } else if (_x983 == _root982) {
                                _x983 = null;
                                break;
                            } else {
                                _descend984 = false;
                                _from_left985 = !(_x983._parent9 == null) && _x983 == _x983._parent9._left7;
                                _x983 = _x983._parent9;
                            }
                        } else {
                            if (_x983 == _root982) {
                                _x983 = null;
                                break;
                            } else {
                                _descend984 = false;
                                _from_left985 = !(_x983._parent9 == null) && _x983 == _x983._parent9._left7;
                                _x983 = _x983._parent9;
                            }
                        }
                    }
                    _new_x981 = _x983;
                    var _mp986 = _x983._parent9;
                    var _mr987 = _x983._right8;
                    /* replace _x983 with _mr987 in _mp986 */
                    if (!(_mp986 == null)) {
                        if (_mp986._left7 == _x983) {
                            _mp986._left7 = _mr987;
                        } else {
                            _mp986._right8 = _mr987;
                        }
                    }
                    if (!(_mr987 == null)) {
                        _mr987._parent9 = _mp986;
                    }
                    /* replace _to_remove977 with _x983 in _parent978 */
                    if (!(_parent978 == null)) {
                        if (_parent978._left7 == _to_remove977) {
                            _parent978._left7 = _x983;
                        } else {
                            _parent978._right8 = _x983;
                        }
                    }
                    if (!(_x983 == null)) {
                        _x983._parent9 = _parent978;
                    }
                    /* replace null with _left979 in _x983 */
                    _x983._left7 = _left979;
                    if (!(_left979 == null)) {
                        _left979._parent9 = _x983;
                    }
                    /* replace _mr987 with (_to_remove977)._right8 in _x983 */
                    _x983._right8 = _to_remove977._right8;
                    if (!(_to_remove977._right8 == null)) {
                        _to_remove977._right8._parent9 = _x983;
                    }
                    /* _min_ax12 is min of ax1 */
                    var _augval988 = _x983.ax1;
                    var _child989 = _x983._left7;
                    if (!(_child989 == null)) {
                        var _val990 = _child989._min_ax12;
                        _augval988 = _augval988 < _val990 ? _augval988 : _val990;
                    }
                    var _child991 = _x983._right8;
                    if (!(_child991 == null)) {
                        var _val992 = _child991._min_ax12;
                        _augval988 = _augval988 < _val992 ? _augval988 : _val992;
                    }
                    _x983._min_ax12 = _augval988;
                    /* _min_ay13 is min of ay1 */
                    var _augval993 = _x983.ay1;
                    var _child994 = _x983._left7;
                    if (!(_child994 == null)) {
                        var _val995 = _child994._min_ay13;
                        _augval993 = _augval993 < _val995 ? _augval993 : _val995;
                    }
                    var _child996 = _x983._right8;
                    if (!(_child996 == null)) {
                        var _val997 = _child996._min_ay13;
                        _augval993 = _augval993 < _val997 ? _augval993 : _val997;
                    }
                    _x983._min_ay13 = _augval993;
                    /* _max_ay24 is max of ay2 */
                    var _augval998 = _x983.ay2;
                    var _child999 = _x983._left7;
                    if (!(_child999 == null)) {
                        var _val1000 = _child999._max_ay24;
                        _augval998 = _augval998 < _val1000 ? _val1000 : _augval998;
                    }
                    var _child1001 = _x983._right8;
                    if (!(_child1001 == null)) {
                        var _val1002 = _child1001._max_ay24;
                        _augval998 = _augval998 < _val1002 ? _val1002 : _augval998;
                    }
                    _x983._max_ay24 = _augval998;
                    _x983._height10 = 1 + ((_x983._left7 == null ? -1 : _x983._left7._height10) > (_x983._right8 ==
                            null ? -1 : _x983._right8._height10) ? _x983._left7 == null ? -1 : _x983._left7
                        ._height10 : _x983._right8 == null ? -1 : _x983._right8._height10);
                    var _cursor1003 = _mp986;
                    var _changed1004 = true;
                    while (_changed1004 && !(_cursor1003 == _parent978)) {
                        var _old__min_ax121005 = _cursor1003._min_ax12;
                        var _old__min_ay131006 = _cursor1003._min_ay13;
                        var _old__max_ay241007 = _cursor1003._max_ay24;
                        var _old_height1008 = _cursor1003._height10;
                        /* _min_ax12 is min of ax1 */
                        var _augval1009 = _cursor1003.ax1;
                        var _child1010 = _cursor1003._left7;
                        if (!(_child1010 == null)) {
                            var _val1011 = _child1010._min_ax12;
                            _augval1009 = _augval1009 < _val1011 ? _augval1009 : _val1011;
                        }
                        var _child1012 = _cursor1003._right8;
                        if (!(_child1012 == null)) {
                            var _val1013 = _child1012._min_ax12;
                            _augval1009 = _augval1009 < _val1013 ? _augval1009 : _val1013;
                        }
                        _cursor1003._min_ax12 = _augval1009;
                        /* _min_ay13 is min of ay1 */
                        var _augval1014 = _cursor1003.ay1;
                        var _child1015 = _cursor1003._left7;
                        if (!(_child1015 == null)) {
                            var _val1016 = _child1015._min_ay13;
                            _augval1014 = _augval1014 < _val1016 ? _augval1014 : _val1016;
                        }
                        var _child1017 = _cursor1003._right8;
                        if (!(_child1017 == null)) {
                            var _val1018 = _child1017._min_ay13;
                            _augval1014 = _augval1014 < _val1018 ? _augval1014 : _val1018;
                        }
                        _cursor1003._min_ay13 = _augval1014;
                        /* _max_ay24 is max of ay2 */
                        var _augval1019 = _cursor1003.ay2;
                        var _child1020 = _cursor1003._left7;
                        if (!(_child1020 == null)) {
                            var _val1021 = _child1020._max_ay24;
                            _augval1019 = _augval1019 < _val1021 ? _val1021 : _augval1019;
                        }
                        var _child1022 = _cursor1003._right8;
                        if (!(_child1022 == null)) {
                            var _val1023 = _child1022._max_ay24;
                            _augval1019 = _augval1019 < _val1023 ? _val1023 : _augval1019;
                        }
                        _cursor1003._max_ay24 = _augval1019;
                        _cursor1003._height10 = 1 + ((_cursor1003._left7 == null ? -1 : _cursor1003._left7
                                ._height10) > (_cursor1003._right8 == null ? -1 : _cursor1003._right8
                            ._height10) ? _cursor1003._left7 == null ? -1 : _cursor1003._left7._height10 :
                            _cursor1003._right8 == null ? -1 : _cursor1003._right8._height10);
                        _changed1004 = false;
                        _changed1004 = _changed1004 || !(_old__min_ax121005 == _cursor1003._min_ax12);
                        _changed1004 = _changed1004 || !(_old__min_ay131006 == _cursor1003._min_ay13);
                        _changed1004 = _changed1004 || !(_old__max_ay241007 == _cursor1003._max_ay24);
                        _changed1004 = _changed1004 || !(_old_height1008 == _cursor1003._height10);
                        _cursor1003 = _cursor1003._parent9;
                    }
                }
                var _cursor1024 = _parent978;
                var _changed1025 = true;
                while (_changed1025 && !(_cursor1024 == null)) {
                    var _old__min_ax121026 = _cursor1024._min_ax12;
                    var _old__min_ay131027 = _cursor1024._min_ay13;
                    var _old__max_ay241028 = _cursor1024._max_ay24;
                    var _old_height1029 = _cursor1024._height10;
                    /* _min_ax12 is min of ax1 */
                    var _augval1030 = _cursor1024.ax1;
                    var _child1031 = _cursor1024._left7;
                    if (!(_child1031 == null)) {
                        var _val1032 = _child1031._min_ax12;
                        _augval1030 = _augval1030 < _val1032 ? _augval1030 : _val1032;
                    }
                    var _child1033 = _cursor1024._right8;
                    if (!(_child1033 == null)) {
                        var _val1034 = _child1033._min_ax12;
                        _augval1030 = _augval1030 < _val1034 ? _augval1030 : _val1034;
                    }
                    _cursor1024._min_ax12 = _augval1030;
                    /* _min_ay13 is min of ay1 */
                    var _augval1035 = _cursor1024.ay1;
                    var _child1036 = _cursor1024._left7;
                    if (!(_child1036 == null)) {
                        var _val1037 = _child1036._min_ay13;
                        _augval1035 = _augval1035 < _val1037 ? _augval1035 : _val1037;
                    }
                    var _child1038 = _cursor1024._right8;
                    if (!(_child1038 == null)) {
                        var _val1039 = _child1038._min_ay13;
                        _augval1035 = _augval1035 < _val1039 ? _augval1035 : _val1039;
                    }
                    _cursor1024._min_ay13 = _augval1035;
                    /* _max_ay24 is max of ay2 */
                    var _augval1040 = _cursor1024.ay2;
                    var _child1041 = _cursor1024._left7;
                    if (!(_child1041 == null)) {
                        var _val1042 = _child1041._max_ay24;
                        _augval1040 = _augval1040 < _val1042 ? _val1042 : _augval1040;
                    }
                    var _child1043 = _cursor1024._right8;
                    if (!(_child1043 == null)) {
                        var _val1044 = _child1043._max_ay24;
                        _augval1040 = _augval1040 < _val1044 ? _val1044 : _augval1040;
                    }
                    _cursor1024._max_ay24 = _augval1040;
                    _cursor1024._height10 = 1 + ((_cursor1024._left7 == null ? -1 : _cursor1024._left7._height10) >
                        (_cursor1024._right8 == null ? -1 : _cursor1024._right8._height10) ? _cursor1024
                        ._left7 == null ? -1 : _cursor1024._left7._height10 : _cursor1024._right8 == null ? -1 :
                        _cursor1024._right8._height10);
                    _changed1025 = false;
                    _changed1025 = _changed1025 || !(_old__min_ax121026 == _cursor1024._min_ax12);
                    _changed1025 = _changed1025 || !(_old__min_ay131027 == _cursor1024._min_ay13);
                    _changed1025 = _changed1025 || !(_old__max_ay241028 == _cursor1024._max_ay24);
                    _changed1025 = _changed1025 || !(_old_height1029 == _cursor1024._height10);
                    _cursor1024 = _cursor1024._parent9;
                }
                if (this._root1 == _to_remove977) {
                    this._root1 = _new_x981;
                }
                _prev_cursor5 = null;
            }
        }
    };
    buildViz = (function (d3) {
        return function (widthInPixels = 1000, heightInPixels = 600, max_snippets = null, color = null,
            sortByDist = true, useFullDoc = false, greyZeroScores = false, asianMode = false,
            nonTextFeaturesMode = false, showCharacteristic = true, wordVecMaxPValue = false,
            saveSvgButton = false, reverseSortScoresForNotCategory = false, minPVal = 0.1, pValueColors =
            false, xLabelText = null, yLabelText = null, fullData = null, showTopTerms = true, showNeutral =
            false, getTooltipContent = null, xAxisValues = null, yAxisValues = null, colorFunc = null,
            showAxes = true, showExtra = false, doCensorPoints = true, centerLabelsOverPoints = false,
            xAxisLabels = null, yAxisLabels = null, topic_model_preview_size = 10, verticalLines = null,
            horizontal_line_y_position = null, vertical_line_x_position = null, unifiedContexts = false,
            showCategoryHeadings = true, showCrossAxes = true, divName = "d3-div-1", alternativeTermFunc =
            null, includeAllContexts = false, showAxesAndCrossHairs = false, x_axis_values_format = ".3f",
            y_axis_values_format = ".3f", matchFullLine = false, maxOverlapping = -1, showCorpusStats =
            true, sortDocLabelsByName = false, alwaysJump = true, highlightSelectedCategory = false,
            showDiagonal = false, useGlobalScale = false, enableTermCategoryDescription = true,
            getCustomTermHtml = null, headerNames = null, headerSortingAlgos = null, ignoreCategories =
            false, backgroundLabels = null, labelPriorityColumn = null, textColorColumn = undefined,
            suppressTextColumn = undefined, backgroundColor = undefined, censorPointColumn = undefined,
            rightOrderColumn = undefined, subwordEncoding = null) {
            function formatTermForDisplay(term) {
                if (subwordEncoding === "RoBERTa" && (term.charCodeAt(0) === 288 || term.charCodeAt(0) ===
                        289)) term = "_" + term.substr(1, term.length - 1);
                return term;
            }
            //var divName = 'd3-div-1';
            // Set the dimensions of the canvas / graph
            var padding = {
                top: 30,
                right: 20,
                bottom: 30,
                left: 50,
            };
            if (!showAxes) {
                padding = {
                    top: 30,
                    right: 20,
                    bottom: 30,
                    left: 50,
                };
            }
            var margin = padding,
                width = widthInPixels - margin.left - margin.right,
                height = heightInPixels - margin.top - margin.bottom;
            fullData.data.forEach(function (x, i) {
                x.i = i;
            });
            // Set the ranges
            var x = d3.scaleLinear().range([0, width]);
            var y = d3.scaleLinear().range([height, 0]);
            if (unifiedContexts) {
                document.querySelectorAll("#" + divName + "-" + "notcol").forEach(function (x) {
                    x.style.display = "none";
                });
                document.querySelectorAll("." + divName + "-" + "contexts").forEach(function (x) {
                    x.style.width = "90%";
                });
            } else if (showNeutral) {
                if (showExtra) {
                    document.querySelectorAll("." + divName + "-" + "contexts").forEach(function (x) {
                        x.style.width = "25%";
                        x.style.float = "left";
                    });
                    ["notcol", "neutcol", "extracol"].forEach(function (columnName) {
                        document.querySelectorAll("#" + divName + "-" + columnName).forEach(
                            function (x) {
                                x.style.display = "inline";
                                x.style.float = "left";
                                x.style.width = "25%";
                            });
                    });
                } else {
                    document.querySelectorAll("." + divName + "-" + "contexts").forEach(function (x) {
                        x.style.width = "33%";
                        x.style.float = "left";
                    });
                    ["notcol", "neutcol"].forEach(function (columnName) {
                        document.querySelectorAll("#" + divName + "-" + columnName).forEach(
                            function (x) {
                                x.style.display = "inline";
                                x.style.float = "left";
                                x.style.width = "33%";
                            });
                    });
                }
            } else {
                document.querySelectorAll("." + divName + "-" + "contexts").forEach(function (x) {
                    x.style.width = "45%";
                    //x.style.display = 'inline'
                    x.style.float = "left";
                });
                ["notcol"].forEach(function (columnName) {
                    document.querySelectorAll("#" + divName + "-" + columnName).forEach(function (
                    x) {
                        //x.style.display = 'inline'
                        x.style.float = "left";
                        x.style.width = "45%";
                    });
                });
            }
            var yAxis = null;
            var xAxis = null;

            function axisLabelerFactory(axis) {
                if (
                    (axis == "x" && xLabelText == null) || (axis == "y" && yLabelText == null))
                return function (d, i) {
                        return ["Infrequent", "Average", "Frequent"][i];
                    };
                return function (d, i) {
                    return ["Low", "Medium", "High"][i];
                };
            }

            function bs(ar, x) {
                function bsa(s, e) {
                    var mid = Math.floor((s + e) / 2);
                    var midval = ar[mid];
                    if (s == e) {
                        return s;
                    }
                    if (midval == x) {
                        return mid;
                    } else if (midval < x) {
                        return bsa(mid + 1, e);
                    } else {
                        return bsa(s, mid);
                    }
                }
                return bsa(0, ar.length);
            }
            console.log("fullData");
            console.log(fullData);
            var sortedX = fullData.data.map((x) => x).sort(function (a, b) {
                return a.x < b.x ? -1 : a.x == b.x ? 0 : 1;
            }).map(function (x) {
                return x.x;
            });
            var sortedOx = fullData.data.map((x) => x).sort(function (a, b) {
                return a.ox < b.ox ? -1 : a.ox == b.ox ? 0 : 1;
            }).map(function (x) {
                return x.ox;
            });
            var sortedY = fullData.data.map((x) => x).sort(function (a, b) {
                return a.y < b.y ? -1 : a.y == b.y ? 0 : 1;
            }).map(function (x) {
                return x.y;
            });
            var sortedOy = fullData.data.map((x) => x).sort(function (a, b) {
                return a.oy < b.oy ? -1 : a.oy == b.oy ? 0 : 1;
            }).map(function (x) {
                return x.oy;
            });
            console.log(fullData.data[0]);

            function labelWithZScore(axis, axisName, tickPoints, axis_values_format) {
                var myVals = axisName === "x" ? sortedOx : sortedOy;
                var myPlotedVals = axisName === "x" ? sortedX : sortedY;
                var ticks = tickPoints.map(function (x) {
                    return myPlotedVals[bs(myVals, x)];
                });
                return axis.tickValues(ticks).tickFormat(function (d, i) {
                    return d3.format(axis_values_format)(tickPoints[i]);
                });
            }
            if (xAxisValues) {
                xAxis = labelWithZScore(d3.axisBottom(x), "x", xAxisValues, x_axis_values_format);
            } else if (xAxisLabels) {
                xAxis = d3.axisBottom(x).ticks(xAxisLabels.length).tickFormat(function (d, i) {
                    return xAxisLabels[i];
                });
            } else {
                xAxis = d3.axisBottom(x).ticks(3).tickFormat(axisLabelerFactory("x"));
            }
            if (yAxisValues) {
                yAxis = labelWithZScore(d3.axisLeft(y), "y", yAxisValues, y_axis_values_format);
            } else if (yAxisLabels) {
                yAxis = d3.axisLeft(y).ticks(yAxisLabels.length).tickFormat(function (d, i) {
                    return yAxisLabels[i];
                });
            } else {
                yAxis = d3.axisLeft(y).ticks(3).tickFormat(axisLabelerFactory("y"));
            }
            // var label = d3.select("body").append("div")
            var label = d3.select("#" + divName).append("div").attr("class", "label");
            var interpolateLightGreys = d3.interpolate(d3.rgb(230, 230, 230), d3.rgb(130, 130, 130));
            // setup fill color
            if (color == null) {
                color = d3.interpolateRdYlBu;
            }
            if (headerNames !== undefined && headerNames !== null && headerSortingAlgos !== undefined &&
                headerSortingAlgos !== null) {
                showTopTerms = true;
            }
            var pixelsToAddToWidth = 200;
            if (!showTopTerms && !showCharacteristic) {
                pixelsToAddToWidth = 0;
            }
            if (backgroundColor !== undefined) {
                document.body.style.backgroundColor = backgroundColor;
            }
            // Adds the svg canvas
            // var svg = d3.select("body")
            svg = d3.select("#" + divName).append("svg").attr("width", width + margin.left + margin.right +
                    pixelsToAddToWidth).attr("height", height + margin.top + margin.bottom).append("g")
                .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
            origSVGLeft = svg.node().getBoundingClientRect().left;
            origSVGTop = svg.node().getBoundingClientRect().top;
            var lastCircleSelected = null;

            function getCorpusWordCounts() {
                var binaryLabels = fullData.docs.labels.map(function (label) {
                    return (1 * (fullData.docs.categories[label] != fullData.info
                        .category_internal_name));
                });
                var wordCounts = {}; // word -> [cat counts, not-cat-counts]
                var wordCountSums = [0, 0];
                fullData.docs.texts.forEach(function (text, i) {
                    text.toLowerCase().trim().split(/\W+/).forEach(function (word) {
                        if (word.trim() !== "") {
                            if (!(word in wordCounts)) wordCounts[word] = [0, 0];
                            wordCounts[word][binaryLabels[i]]++;
                            wordCountSums[binaryLabels[i]]++;
                        }
                    });
                });
                return {
                    avgDocLen: (wordCountSums[0] + wordCountSums[1]) / fullData.docs.texts.length,
                    counts: wordCounts,
                    sums: wordCountSums,
                    uniques: [
                        [0, 0]
                    ].concat(Object.keys(wordCounts).map(function (key) {
                        return wordCounts[key];
                    })).reduce(function (a, b) {
                        return [a[0] + (b[0] > 0), a[1] + (b[1] > 0)];
                    }),
                };
            }

            function getContextWordCounts(query) {
                var wordCounts = {};
                var wordCountSums = [0, 0];
                var priorCountSums = [0, 0];
                gatherTermContexts(termDict[query]).contexts.forEach(function (contextSet, categoryIdx) {
                    contextSet.forEach(function (context) {
                        context.snippets.forEach(function (snippet) {
                            var tokens = snippet.toLowerCase().trim().replace("<b>",
                                "").replace("</b>", "").split(/\W+/);
                            var matchIndices = [];
                            tokens.forEach(function (word, i) {
                                if (word === query) matchIndices.push(i);
                            });
                            tokens.forEach(function (word, i) {
                                if (word.trim() !== "") {
                                    var isValid = false;
                                    for (var matchI in matchIndices) {
                                        if (Math.abs(i - matchI) < 3) {
                                            isValid = true;
                                            break;
                                        }
                                    }
                                    if (isValid) {
                                        //console.log([word, i, matchI, isValid]);
                                        if (!(word in wordCounts)) {
                                            var priorCounts =
                                                corpusWordCounts.counts[
                                                    word];
                                            wordCounts[word] = [0, 0]
                                                .concat(priorCounts);
                                            priorCountSums[0] +=
                                                priorCounts[0];
                                            priorCountSums[1] +=
                                                priorCounts[1];
                                        }
                                        wordCounts[word][categoryIdx]++;
                                        wordCountSums[categoryIdx]++;
                                    }
                                }
                            });
                        });
                    });
                });
                return {
                    counts: wordCounts,
                    priorSums: priorCountSums,
                    sums: wordCountSums,
                    uniques: [
                        [0, 0]
                    ].concat(Object.keys(wordCounts).map(function (key) {
                        return wordCounts[key];
                    })).reduce(function (a, b) {
                        return [a[0] + (b[0] > 0), a[1] + (b[1] > 0)];
                    }),
                };
            }

            function denseRank(ar) {
                var markedAr = ar.map((x, i) => [x, i]).sort((a, b) => a[0] - b[0]);
                var curRank = 1;
                var rankedAr = markedAr.map(function (x, i) {
                    if (i > 0 && x[0] != markedAr[i - 1][0]) {
                        curRank++;
                    }
                    return [curRank, x[0], x[1]];
                });
                return rankedAr.map((x) => x).sort((a, b) => a[2] - b[2]).map((x) => x[0]);
            }

            function getDenseRanks(fullData, categoryNum) {
                console.log("GETTING DENSE RANKS");
                console.log("CAT NUM " + categoryNum);
                console.log(fullData);
                var fgFreqs = Array(fullData.data.length).fill(0);
                var bgFreqs = Array(fullData.data.length).fill(0);
                var categoryTermCounts = fullData.termCounts[categoryNum];
                Object.keys(categoryTermCounts).forEach(
                    (key) => (fgFreqs[key] = categoryTermCounts[key][0]));
                fullData.termCounts.forEach(function (categoryTermCounts, otherCategoryNum) {
                    if (otherCategoryNum != categoryNum) {
                        Object.keys(categoryTermCounts).forEach(
                            (key) => (bgFreqs[key] += categoryTermCounts[key][0]));
                    }
                });
                var fgDenseRanks = denseRank(fgFreqs);
                var bgDenseRanks = denseRank(bgFreqs);
                var maxfgDenseRanks = Math.max(...fgDenseRanks);
                var minfgDenseRanks = Math.min(...fgDenseRanks);
                var scalefgDenseRanks = fgDenseRanks.map(
                    (x) => (x - minfgDenseRanks) / (maxfgDenseRanks - minfgDenseRanks));
                var maxbgDenseRanks = Math.max(...bgDenseRanks);
                var minbgDenseRanks = Math.min(...bgDenseRanks);
                var scalebgDenseRanks = bgDenseRanks.map(
                    (x) => (x - minbgDenseRanks) / (maxbgDenseRanks - minbgDenseRanks));
                return {
                    fg: scalefgDenseRanks,
                    bg: scalebgDenseRanks,
                    bgFreqs: bgFreqs,
                    fgFreqs: fgFreqs,
                    term: fullData.data.map((x) => x.term),
                };
            }

            function getCategoryDenseRankScores(fullData, categoryNum) {
                var denseRanks = getDenseRanks(fullData, categoryNum);
                return denseRanks.fg.map((x, i) => x - denseRanks.bg[i]);
            }

            function getTermCounts(fullData) {
                var counts = Array(fullData.data.length).fill(0);
                fullData.termCounts.forEach(function (categoryTermCounts) {
                    Object.keys(categoryTermCounts).forEach(
                        (key) => (counts[key] = categoryTermCounts[key][0]));
                });
                return counts;
            }

            function getContextWordLORIPs(query) {
                var contextWordCounts = getContextWordCounts(query);
                var ni_k = contextWordCounts.sums[0];
                var nj_k = contextWordCounts.sums[1];
                var n = ni_k + nj_k;
                //var ai_k0 = contextWordCounts.priorSums[0] + contextWordCounts.priorSums[1];
                //var aj_k0 = contextWordCounts.priorSums[0] + contextWordCounts.priorSums[1];
                var a0 = 0.00001; //corpusWordCounts.avgDocLen;
                var a_k0 = Object.keys(contextWordCounts.counts).map(function (x) {
                    var counts = contextWordCounts.counts[x];
                    return (
                        (a0 * (counts[2] + counts[3])) / (contextWordCounts.priorSums[0] +
                            contextWordCounts.priorSums[1]));
                }).reduce(function (a, b) {
                    return a + b;
                });
                var ai_k0 = a_k0 / ni_k;
                var aj_k0 = a_k0 / nj_k;
                var scores = Object.keys(contextWordCounts.counts).map(function (word) {
                    var countData = contextWordCounts.counts[word];
                    var yi = countData[0];
                    var yj = countData[1];
                    //var ai = countData[2];
                    //var aj = countData[3];
                    //var ai = countData[2] + countData[3];
                    //var aj = ai;
                    //var ai = (countData[2] + countData[3]) * a0/ni_k;
                    //var aj = (countData[2] + countData[3]) * a0/nj_k;
                    var ai = (a0 * (countData[2] + countData[3])) / (contextWordCounts.priorSums[
                        0] + contextWordCounts.priorSums[1]);
                    var aj = ai;
                    var deltahat_i_j = +Math.log(((yi + ai) * 1) / (ni_k + ai_k0 - yi - ai)) - Math
                        .log(((yj + aj) * 1) / (nj_k + aj_k0 - yj - aj));
                    var var_deltahat_i_j = 1 / (yi + ai) + 1 / (ni_k + ai_k0 - yi - ai) + 1 / (yj +
                        aj) + 1 / (nj_k + aj_k0 - yj - aj);
                    var zeta_ij = deltahat_i_j / Math.sqrt(var_deltahat_i_j);
                    return [word, yi, yj, ai, aj, ai_k0, zeta_ij];
                }).sort(function (a, b) {
                    return b[5] - a[5];
                });
                return scores;
            }

            function getContextWordSFS(query) {
                // from https://stackoverflow.com/questions/14846767/std-normal-cdf-normal-cdf-or-error-function
                function cdf(x, mean, variance) {
                    return 0.5 * (1 + erf((x - mean) / Math.sqrt(2 * variance)));
                }

                function erf(x) {
                    // save the sign of x
                    var sign = x >= 0 ? 1 : -1;
                    x = Math.abs(x);
                    // constants
                    var a1 = 0.254829592;
                    var a2 = -0.284496736;
                    var a3 = 1.421413741;
                    var a4 = -1.453152027;
                    var a5 = 1.061405429;
                    var p = 0.3275911;
                    // A&S formula 7.1.26
                    var t = 1.0 / (1.0 + p * x);
                    var y = 1.0 - ((((a5 * t + a4) * t + a3) * t + a2) * t + a1) * t * Math.exp(-x * x);
                    return sign * y; // erf(-x) = -erf(x);
                }

                function scale(a) {
                    return Math.log(a + 0.0000001);
                }
                var contextWordCounts = getContextWordCounts(query);
                var wordList = Object.keys(contextWordCounts.counts).map(function (word) {
                    return contextWordCounts.counts[word].concat([word]);
                });
                var cat_freq_xbar = wordList.map(function (x) {
                    return scale(x[0]);
                }).reduce(function (a, b) {
                    return a + b;
                }) / wordList.length;
                var cat_freq_var = wordList.map(function (x) {
                    return Math.pow(scale(x[0]) - cat_freq_xbar, 2);
                }).reduce(function (a, b) {
                    return a + b;
                }) / wordList.length;
                var cat_prec_xbar = wordList.map(function (x) {
                    return scale(x[0] / (x[0] + x[1]));
                }).reduce(function (a, b) {
                    return a + b;
                }) / wordList.length;
                var cat_prec_var = wordList.map(function (x) {
                    return Math.pow(scale(x[0] / (x[0] + x[1])) - cat_prec_xbar, 2);
                }).reduce(function (a, b) {
                    return a + b;
                }) / wordList.length;
                var ncat_freq_xbar = wordList.map(function (x) {
                    return scale(x[0]);
                }).reduce(function (a, b) {
                    return a + b;
                }) / wordList.length;
                var ncat_freq_var = wordList.map(function (x) {
                    return Math.pow(scale(x[0]) - ncat_freq_xbar, 2);
                }).reduce(function (a, b) {
                    return a + b;
                }) / wordList.length;
                var ncat_prec_xbar = wordList.map(function (x) {
                    return scale(x[0] / (x[0] + x[1]));
                }).reduce(function (a, b) {
                    return a + b;
                }) / wordList.length;
                var ncat_prec_var = wordList.map(function (x) {
                    return Math.pow(scale(x[0] / (x[0] + x[1])) - ncat_prec_xbar, 2);
                }).reduce(function (a, b) {
                    return a + b;
                }) / wordList.length;

                function scaledFScore(cnt, other, freq_xbar, freq_var, prec_xbar, prec_var) {
                    var beta = 1.5;
                    var normFreq = cdf(scale(cnt), freq_xbar, freq_var);
                    var normPrec = cdf(scale(cnt / (cnt + other)), prec_xbar, prec_var);
                    return (
                        ((1 + Math.pow(beta, 2)) * normFreq * normPrec) / (Math.pow(beta, 2) *
                            normFreq + normPrec));
                }
                var sfs = wordList.map(function (x) {
                    cat_sfs = scaledFScore(x[0], x[1], cat_freq_xbar, cat_freq_var, cat_prec_xbar,
                        cat_prec_var);
                    ncat_sfs = scaledFScore(x[1], x[0], ncat_freq_xbar, ncat_freq_var,
                        ncat_prec_xbar, ncat_prec_var);
                    return [cat_sfs > ncat_sfs ? cat_sfs : -ncat_sfs].concat(x);
                }).sort(function (a, b) {
                    return b[0] - a[0];
                });
                return sfs;
            }

            function deselectLastCircle() {
                if (lastCircleSelected) {
                    lastCircleSelected.style["stroke"] = null;
                    lastCircleSelected = null;
                }
            }

            function getSentenceBoundaries(text) {
                // !!! need to use spacy's sentence splitter
                if (asianMode) {
                    var sentenceRe = /\n/gim;
                } else {
                    var sentenceRe = /\(?[^\.\?\!\n\b]+[\n\.!\?]\)?/g;
                }
                var offsets = [];
                var match;
                while ((match = sentenceRe.exec(text)) != null) {
                    offsets.push(match.index);
                }
                offsets.push(text.length);
                return offsets;
            }

            function getMatchingSnippet(text, boundaries, start, end) {
                var sentenceStart = null;
                var sentenceEnd = null;
                for (var i in boundaries) {
                    var position = boundaries[i];
                    if (position <= start && (sentenceStart == null || position > sentenceStart)) {
                        sentenceStart = position;
                    }
                    if (position >= end) {
                        sentenceEnd = position;
                        break;
                    }
                }
                var snippet = (text.slice(sentenceStart, start) + "<b>" + text.slice(start, end) + "</b>" +
                    text.slice(end, sentenceEnd)).trim();
                if (sentenceStart == null) {
                    sentenceStart = 0;
                }
                return {
                    snippet: snippet,
                    sentenceStart: sentenceStart,
                };
            }

            function gatherTermContexts(d, includeAll = true) {
                var category_name = fullData["info"]["category_name"];
                var not_category_name = fullData["info"]["not_category_name"];
                var matches = [
                    [],
                    [],
                    [],
                    []
                ];
                console.log("searching");
                if (fullData.docs === undefined) return matches;
                if (!nonTextFeaturesMode) {
                    return searchInText(d, includeAll);
                } else {
                    return searchInExtraFeatures(d, includeAll);
                }
            }

            function searchInExtraFeatures(d) {
                var matches = [
                    [],
                    [],
                    [],
                    []
                ];
                var term = d.term;
                var categoryNum = fullData.docs.categories.indexOf(fullData.info.category_internal_name);
                var notCategoryNumList = fullData.docs.categories.map(function (x, i) {
                    if (fullData.info.not_category_internal_names.indexOf(x) > -1) {
                        return i;
                    } else {
                        return -1;
                    }
                }).filter(function (x) {
                    return x > -1;
                });
                var neutralCategoryNumList = fullData.docs.categories.map(function (x, i) {
                    if (fullData.info.neutral_category_internal_names.indexOf(x) > -1) {
                        return i;
                    } else {
                        return -1;
                    }
                }).filter(function (x) {
                    return x > -1;
                });
                var extraCategoryNumList = fullData.docs.categories.map(function (x, i) {
                    if (fullData.info.extra_category_internal_names.indexOf(x) > -1) {
                        return i;
                    } else {
                        return -1;
                    }
                }).filter(function (x) {
                    return x > -1;
                });
                var pattern = null;
                if ("metalists" in fullData && term in fullData.metalists) {
                    // from https://stackoverflow.com/questions/3446170/escape-string-for-use-in-javascript-regex
                    function escapeRegExp(str) {
                        return str.replace(/[\\?\-\[\]\/\{\}\(\)\*\+\?\.\\\^\$\|\']/g, "\\$&");
                    }
                    console.log("term");
                    console.log(term);
                    pattern = new RegExp("\\W(" + fullData.metalists[term].map(escapeRegExp).join("|") +
                        ")\\W", "gim");
                }
                for (var i in fullData.docs.extra) {
                    if (term in fullData.docs.extra[i]) {
                        var strength = fullData.docs.extra[i][term] / Object.values(fullData.docs.extra[i])
                            .reduce(function (a, b) {
                                return a + b;
                            });
                        var docLabel = fullData.docs.labels[i];
                        var numericLabel = -1;
                        if (docLabel == categoryNum) {
                            numericLabel = 0;
                        } else if (notCategoryNumList.indexOf(docLabel) > -1) {
                            numericLabel = 1;
                        } else if (neutralCategoryNumList.indexOf(docLabel) > -1) {
                            numericLabel = 2;
                        } else if (extraCategoryNumList.indexOf(docLabel) > -1) {
                            numericLabel = 3;
                        }
                        if (numericLabel == -1) {
                            continue;
                        }
                        var text = fullData.docs.texts[i];
                        if (fullData.offsets !== undefined) {
                            if (fullData.offsets[term] !== undefined && fullData.offsets[term][i] !==
                                undefined) {
                                var curMatch = {
                                    id: i,
                                    snippets: [],
                                    strength: strength,
                                    docLabel: docLabel,
                                    meta: fullData.docs.meta ? fullData.docs.meta[i] : "",
                                };
                                for (const offset_i in fullData.offsets[term][i]) {
                                    var offset = fullData.offsets[term][i][offset_i];
                                    var spanStart = Math.max(offset[0] - 50, 0);
                                    var spanEnd = Math.min(50, text.length - offset[1]);
                                    var leftContext = text.substr(spanStart, offset[0] - spanStart);
                                    var matchStr = text.substr(offset[0], offset[1] - offset[0]);
                                    var rightContext = text.substr(offset[1], spanEnd);
                                    var snippet = leftContext +
                                        '<b style="background-color: lightgoldenrodyellow">' + matchStr +
                                        "</b>" + rightContext;
                                    if (spanStart > 0) snippet = "..." + snippet;
                                    if (text.length - offset[1] > 50) snippet = snippet + "...";
                                    curMatch.snippets.push(snippet);
                                }
                                matches[numericLabel].push(curMatch);
                            }
                        } else {
                            if (!useFullDoc) text = text.slice(0, 300);
                            if (pattern !== null) {
                                text = text.replace(pattern, "<b>$&</b>");
                            }
                            var curMatch = {
                                id: i,
                                snippets: [text],
                                strength: strength,
                                docLabel: docLabel,
                                meta: fullData.docs.meta ? fullData.docs.meta[i] : "",
                            };
                            matches[numericLabel].push(curMatch);
                        }
                    }
                }
                for (var i in [0, 1]) {
                    matches[i] = matches[i].sort(function (a, b) {
                        return a.strength < b.strength ? 1 : -1;
                    });
                }
                return {
                    contexts: matches,
                    info: d,
                };
            }
            // from https://mathiasbynens.be/notes/es-unicode-property-escapes#emoji
            var emojiRE =
                /(?:[\u261D\u26F9\u270A-\u270D]|\uD83C[\uDF85\uDFC2-\uDFC4\uDFC7\uDFCA-\uDFCC]|\uD83D[\uDC42\uDC43\uDC46-\uDC50\uDC66-\uDC69\uDC6E\uDC70-\uDC78\uDC7C\uDC81-\uDC83\uDC85-\uDC87\uDCAA\uDD74\uDD75\uDD7A\uDD90\uDD95\uDD96\uDE45-\uDE47\uDE4B-\uDE4F\uDEA3\uDEB4-\uDEB6\uDEC0\uDECC]|\uD83E[\uDD18-\uDD1C\uDD1E\uDD1F\uDD26\uDD30-\uDD39\uDD3D\uDD3E\uDDD1-\uDDDD])(?:\uD83C[\uDFFB-\uDFFF])?|(?:[\u231A\u231B\u23E9-\u23EC\u23F0\u23F3\u25FD\u25FE\u2614\u2615\u2648-\u2653\u267F\u2693\u26A1\u26AA\u26AB\u26BD\u26BE\u26C4\u26C5\u26CE\u26D4\u26EA\u26F2\u26F3\u26F5\u26FA\u26FD\u2705\u270A\u270B\u2728\u274C\u274E\u2753-\u2755\u2757\u2795-\u2797\u27B0\u27BF\u2B1B\u2B1C\u2B50\u2B55]|\uD83C[\uDC04\uDCCF\uDD8E\uDD91-\uDD9A\uDDE6-\uDDFF\uDE01\uDE1A\uDE2F\uDE32-\uDE36\uDE38-\uDE3A\uDE50\uDE51\uDF00-\uDF20\uDF2D-\uDF35\uDF37-\uDF7C\uDF7E-\uDF93\uDFA0-\uDFCA\uDFCF-\uDFD3\uDFE0-\uDFF0\uDFF4\uDFF8-\uDFFF]|\uD83D[\uDC00-\uDC3E\uDC40\uDC42-\uDCFC\uDCFF-\uDD3D\uDD4B-\uDD4E\uDD50-\uDD67\uDD7A\uDD95\uDD96\uDDA4\uDDFB-\uDE4F\uDE80-\uDEC5\uDECC\uDED0-\uDED2\uDEEB\uDEEC\uDEF4-\uDEF8]|\uD83E[\uDD10-\uDD3A\uDD3C-\uDD3E\uDD40-\uDD45\uDD47-\uDD4C\uDD50-\uDD6B\uDD80-\uDD97\uDDC0\uDDD0-\uDDE6])|(?:[#\*0-9\xA9\xAE\u203C\u2049\u2122\u2139\u2194-\u2199\u21A9\u21AA\u231A\u231B\u2328\u23CF\u23E9-\u23F3\u23F8-\u23FA\u24C2\u25AA\u25AB\u25B6\u25C0\u25FB-\u25FE\u2600-\u2604\u260E\u2611\u2614\u2615\u2618\u261D\u2620\u2622\u2623\u2626\u262A\u262E\u262F\u2638-\u263A\u2640\u2642\u2648-\u2653\u2660\u2663\u2665\u2666\u2668\u267B\u267F\u2692-\u2697\u2699\u269B\u269C\u26A0\u26A1\u26AA\u26AB\u26B0\u26B1\u26BD\u26BE\u26C4\u26C5\u26C8\u26CE\u26CF\u26D1\u26D3\u26D4\u26E9\u26EA\u26F0-\u26F5\u26F7-\u26FA\u26FD\u2702\u2705\u2708-\u270D\u270F\u2712\u2714\u2716\u271D\u2721\u2728\u2733\u2734\u2744\u2747\u274C\u274E\u2753-\u2755\u2757\u2763\u2764\u2795-\u2797\u27A1\u27B0\u27BF\u2934\u2935\u2B05-\u2B07\u2B1B\u2B1C\u2B50\u2B55\u3030\u303D\u3297\u3299]|\uD83C[\uDC04\uDCCF\uDD70\uDD71\uDD7E\uDD7F\uDD8E\uDD91-\uDD9A\uDDE6-\uDDFF\uDE01\uDE02\uDE1A\uDE2F\uDE32-\uDE3A\uDE50\uDE51\uDF00-\uDF21\uDF24-\uDF93\uDF96\uDF97\uDF99-\uDF9B\uDF9E-\uDFF0\uDFF3-\uDFF5\uDFF7-\uDFFF]|\uD83D[\uDC00-\uDCFD\uDCFF-\uDD3D\uDD49-\uDD4E\uDD50-\uDD67\uDD6F\uDD70\uDD73-\uDD7A\uDD87\uDD8A-\uDD8D\uDD90\uDD95\uDD96\uDDA4\uDDA5\uDDA8\uDDB1\uDDB2\uDDBC\uDDC2-\uDDC4\uDDD1-\uDDD3\uDDDC-\uDDDE\uDDE1\uDDE3\uDDE8\uDDEF\uDDF3\uDDFA-\uDE4F\uDE80-\uDEC5\uDECB-\uDED2\uDEE0-\uDEE5\uDEE9\uDEEB\uDEEC\uDEF0\uDEF3-\uDEF8]|\uD83E[\uDD10-\uDD3A\uDD3C-\uDD3E\uDD40-\uDD45\uDD47-\uDD4C\uDD50-\uDD6B\uDD80-\uDD97\uDDC0\uDDD0-\uDDE6])\uFE0F/g;

            function isEmoji(str) {
                if (str.match(emojiRE)) return true;
                return false;
            }

            function displayObscuredTerms(obscuredTerms, data, term, termInfo, div = "#" + divName + "-" +
                "overlapped-terms") {
                d3.select("#" + divName + "-" + "overlapped-terms").selectAll("div").remove();
                d3.select(div).selectAll("div").remove();
                if (obscuredTerms.length > 1 && maxOverlapping !== 0) {
                    var obscuredDiv = d3.select(div).append("div").attr("class", "obscured").style("align",
                        "center").style("text-align", "center").html('<b>"' + term +
                        '" obstructs</b>: ');
                    obscuredTerms.map(function (term, i) {
                        if (maxOverlapping === -1 || i < maxOverlapping) {
                            makeWordInteractive(data, svg, obscuredDiv.append("text").text(term),
                                term, data.filter((t) => t.term === term)[0], //termInfo
                                false);
                            if (i < obscuredTerms.length - 1 && (maxOverlapping === -1 || i <
                                    maxOverlapping - 1)) {
                                obscuredDiv.append("text").text(", ");
                            }
                        } else if (i === maxOverlapping && i !== obscuredTerms.length - 1) {
                            obscuredDiv.append("text").text("...");
                        }
                    });
                }
            }

            function displayTermContexts(data, termInfo, jump = alwaysJump, includeAll = false) {
                var contexts = termInfo.contexts;
                var info = termInfo.info;
                var notmatches = termInfo.notmatches;
                if (contexts[0].length + contexts[1].length + contexts[2].length + contexts[3].length ==
                    0) {
                    //return null;
                }
                //!!! Future feature: context words
                //var contextWords = getContextWordSFS(info.term);
                //var contextWords = getContextWordLORIPs(info.term);
                //var categoryNames = [fullData.info.category_name,
                //    fullData.info.not_category_name];
                var catInternalName = fullData.info.category_internal_name;

                function addSnippets(contexts, divId, isMatch = true) {
                    var meta = contexts.meta ? contexts.meta : "&nbsp;";
                    var headClass = "snippet_meta docLabel" + contexts.docLabel;
                    var snippetClass = "snippet docLabel" + contexts.docLabel;
                    if (!isMatch) {
                        headClass = "snippet_meta not_match docLabel" + contexts.docLabel;
                        snippetClass = "snippet not_match docLabel" + contexts.docLabel;
                    }
                    d3.select(divId).append("div").attr("class", headClass).html(meta);
                    contexts.snippets.forEach(function (snippet) {
                        d3.select(divId).append("div").attr("class", snippetClass).html(snippet);
                    });
                }
                if (ignoreCategories) {
                    divId = "#" + divName + "-" + "cat";
                    var numMatches = Object.create(null);
                    var temp = d3.select(divId).selectAll("div").remove();
                    var allContexts = contexts[0].concat(contexts[1]).concat(contexts[2]).concat(contexts[
                        3]);
                    var allNotMatches = [];
                    if (notmatches !== undefined) allNotMatches = notmatches[0].concat(notmatches[1])
                        .concat(notmatches[2]).concat(notmatches[3]);
                    d3.select("#" + divName + "-" + "categoryinfo").selectAll("div").remove();
                    var numDocs = fullData.docs.texts.length.toLocaleString("en");
                    var numMatches = allContexts.length;
                    d3.select(divId).append("div").attr("class", "topic_preview").attr("text-align",
                        "center").html("Matched " + numMatches + " out of " + numDocs + " documents: " +
                        ((100 * numMatches) / numDocs).toFixed(2) + "%");
                    if (allContexts.length > 0) {
                        var headerClassName = "text_header";
                        allContexts.forEach(function (singleDoc) {
                            addSnippets(singleDoc, divId);
                        });
                        if (includeAll) {
                            allNotMatches.forEach(function (singleDoc) {
                                addSnippets(singleDoc, divId, false);
                            });
                        }
                    }
                } else if (unifiedContexts) {
                    divId = "#" + divName + "-" + "cat";
                    var docLabelCounts = fullData.docs.labels.reduce(function (map, label) {
                        map[label] = (map[label] || 0) + 1;
                        return map;
                    }, Object.create(null));
                    var numMatches = Object.create(null);
                    var temp = d3.select(divId).selectAll("div").remove();
                    var allContexts = contexts[0].concat(contexts[1]).concat(contexts[2]).concat(contexts[
                        3]);
                    allContexts.forEach(function (singleDoc) {
                        numMatches[singleDoc.docLabel] = (numMatches[singleDoc.docLabel] || 0) + 1;
                    });
                    var allNotMatches = [];
                    if (notmatches !== undefined) allNotMatches = notmatches[0].concat(notmatches[1])
                        .concat(notmatches[2]).concat(notmatches[3]);
                    /*contexts.forEach(function(context) {
                                         context.forEach(function (singleDoc) {
                                             numMatches[singleDoc.docLabel] = (numMatches[singleDoc.docLabel]||0) + 1;
                                             addSnippets(singleDoc, divId);
                                         });
                                     });*/
                    console.log("ORDERING !!!!!");
                    console.log(fullData.info.category_name);
                    console.log(sortDocLabelsByName);
                    var docLabelCountsSorted = Object.keys(docLabelCounts).map((key) => ({
                        label: fullData.docs.categories[key],
                        labelNum: key,
                        matches: numMatches[key] || 0,
                        overall: docLabelCounts[key],
                        percent: ((numMatches[key] || 0) * 100) / docLabelCounts[key],
                    })).sort(function (a, b) {
                        if (highlightSelectedCategory) {
                            if (a["label"] === fullData.info.category_name) {
                                return -1;
                            }
                            if (b["label"] === fullData.info.category_name) {
                                return 1;
                            }
                        }
                        if (sortDocLabelsByName) {
                            return a["label"] < b["label"] ? 1 : a["label"] > b["label"] ? -1 : 0;
                        } else {
                            return b.percent - a.percent;
                        }
                    });
                    console.log("docLabelCountsSorted");
                    console.log(docLabelCountsSorted);
                    console.log(numMatches);
                    console.log("#" + divName + "-" + "categoryinfo");
                    d3.select("#" + divName + "-" + "categoryinfo").selectAll("div").remove();
                    if (showCategoryHeadings) {
                        d3.select("#" + divName + "-" + "categoryinfo").attr("display", "inline");
                    }

                    function getCategoryStatsHTML(counts) {
                        return (counts.matches + " document" + (counts.matches == 1 ? "" : "s") +
                            " out of " + counts.overall + ": " + counts["percent"].toFixed(2) + "%");
                    }

                    function getCategoryInlineHeadingHTML(counts) {
                        return ('<a name="' + divName + "-category" + counts.labelNum + '"></a>' + (
                                ignoreCategories ? "" : counts.label + ": ") +
                            "<span class=topic_preview>" + getCategoryStatsHTML(counts) + "</span>");
                    }
                    docLabelCountsSorted.forEach(function (counts) {
                        var htmlToAdd = "";
                        if (!ignoreCategories) {
                            htmlToAdd += "<b>" + counts.label + "</b>: " + getCategoryStatsHTML(
                                counts);
                        }
                        if (counts.matches > 0) {
                            var headerClassName = "text_header";
                            if (counts.label === fullData.info.category_name &&
                                highlightSelectedCategory) {
                                d3.select(divId).append("div").attr("class", "separator").html(
                                    "<b>Selected category</b>");
                            }
                            d3.select(divId).append("div").attr("class", headerClassName).html(
                                getCategoryInlineHeadingHTML(counts));
                            allContexts.filter((singleDoc) => singleDoc.docLabel == counts.labelNum)
                                .forEach(function (singleDoc) {
                                    addSnippets(singleDoc, divId);
                                });
                            if (includeAll) {
                                allNotMatches.filter((singleDoc) => singleDoc.docLabel == counts
                                    .labelNum).forEach(function (singleDoc) {
                                    addSnippets(singleDoc, divId, false);
                                });
                            }
                            if (counts.label === fullData.info.category_name &&
                                highlightSelectedCategory) {
                                d3.select(divId).append("div").attr("class", "separator").html(
                                    "<b>End selected category</b>");
                                d3.select(divId).append("div").html("<br />");
                            }
                        }
                        if (showCategoryHeadings) {
                            d3.select("#" + divName + "-" + "categoryinfo").attr("display",
                                "inline").append("div").html(htmlToAdd).on("click",
                        function () {
                                window.location.hash = "#" + divName + "-" + "category" +
                                    counts.labelNum;
                            });
                        }
                    });
                } else {
                    var contextColumns = [
                        fullData.info.category_internal_name,
                        fullData.info.not_category_name,
                    ];
                    if (showNeutral) {
                        if ("neutral_category_name" in fullData.info) {
                            contextColumns.push(fullData.info.neutral_category_name);
                        } else {
                            contextColumns.push("Neutral");
                        }
                        if (showExtra) {
                            if ("extra_category_name" in fullData.info) {
                                contextColumns.push(fullData.info.extra_category_name);
                            } else {
                                contextColumns.push("Extra");
                            }
                        }
                    }
                    contextColumns.map(function (catName, catIndex) {
                        if (max_snippets != null) {
                            var contextsToDisplay = contexts[catIndex].slice(0, max_snippets);
                        }
                        //var divId = catName == catInternalName ? '#cat' : '#notcat';
                        var divId = null;
                        if (fullData.info.category_internal_name == catName) {
                            divId = "#" + divName + "-" + "cat";
                        } else if (fullData.info.not_category_name == catName) {
                            divId = "#" + divName + "-" + "notcat";
                        } else if (fullData.info.neutral_category_name == catName) {
                            divId = "#" + divName + "-" + "neut";
                        } else if (fullData.info.extra_category_name == catName) {
                            divId = "#" + divName + "-" + "extra";
                        } else {
                            return;
                        }
                        var temp = d3.select(divId).selectAll("div").remove();
                        contexts[catIndex].forEach(function (context) {
                            addSnippets(context, divId);
                        });
                        if (includeAll) {
                            notmatches[catIndex].forEach(function (context) {
                                addSnippets(context, divId, false);
                            });
                        }
                    });
                }
                var obscuredTerms = getObscuredTerms(data, termInfo.info);
                displayObscuredTerms(obscuredTerms, data, info.term, info, "#" + divName + "-" +
                    "overlapped-terms-clicked");
                d3.select("#" + divName + "-" + "termstats").selectAll("div").remove();
                var termHtml = "Term: <b>" + formatTermForDisplay(info.term) + "</b>";
                if ("metalists" in fullData && info.term in fullData.metalists) {
                    termHtml = "Topic: <b>" + formatTermForDisplay(info.term) + "</b>";
                }
                if (getCustomTermHtml !== null) {
                    termHtml = getCustomTermHtml(info);
                }
                d3.select("#" + divName + "-" + "termstats").append("div").attr("class", "snippet_header")
                    .html(termHtml);
                if ("metalists" in fullData && info.term in fullData.metalists && topic_model_preview_size >
                    0) {
                    d3.select("#" + divName + "-" + "termstats").attr("class", "topic_preview").append(
                        "div").html("<b>Topic preview</b>: " + fullData.metalists[info.term].slice(0,
                        topic_model_preview_size).reduce(function (x, y) {
                        return x + ", " + y;
                    }));
                }
                if ("metadescriptions" in fullData && info.term in fullData.metadescriptions) {
                    d3.select("#" + divName + "-" + "termstats").attr("class", "topic_preview").append(
                        "div").html("<b>Description</b>: " + fullData.metadescriptions[info.term]);
                }
                var message = "";
                var cat_name = fullData.info.category_name;
                var ncat_name = fullData.info.not_category_name;
                var numCatDocs = fullData.docs.labels.map(function (x) {
                    return (
                        (x == fullData.docs.categories.indexOf(fullData.info
                            .category_internal_name)) + 0);
                }).reduce(function (a, b) {
                    return a + b;
                }, 0);
                var notCategoryNumList = fullData.docs.categories.map(function (x, i) {
                    if (fullData.info.not_category_internal_names.indexOf(x) > -1) {
                        return i;
                    } else {
                        return -1;
                    }
                }).filter(function (x) {
                    return x > -1;
                });
                var numNCatDocs = fullData.docs.labels.map(function (x) {
                    return notCategoryNumList.indexOf(x) > -1;
                }).reduce(function (a, b) {
                    return a + b;
                }, 0);

                function getFrequencyDescription(name, count25k, count, ndocs) {
                    var desc = name;
                    if (!enableTermCategoryDescription) {
                        return desc + ":";
                    }
                    desc += " frequency: <div class=text_subhead>" + count25k + " per 25,000 terms</div>";
                    if (!isNaN(Math.round(ndocs))) {
                        desc += "<div class=text_subhead>" + Math.round(ndocs) + " per 1,000 docs</div>";
                    }
                    if (count == 0) {
                        desc += "<u>Not found in any " + name + " documents.</u>";
                    } else {
                        if (!isNaN(Math.round(ndocs))) {
                            desc += "<u>Some of the " + count + " mentions:</u>";
                        } else {
                            desc += count + " mentions";
                        }
                    }
                    /*
                                    desc += '<br><b>Discriminative:</b> ';

                                    desc += contextWords
                                        .slice(cat_name === name ? 0 : contextWords.length - 3,
                                            cat_name === name ? 3 : contextWords.length)
                                        .filter(function (x) {
                                            //return Math.abs(x[5]) > 1.96;
                                            return true;
                                        })
                                        .map(function (x) {return x.join(', ')}).join('<br>');
                                    */
                    return desc;
                }
                if (!unifiedContexts && !ignoreCategories) {
                    console.log("NOT UNIFIED CONTEXTS");
                    d3.select("#" + divName + "-" + "cathead").style("fill", color(1)).html(
                        getFrequencyDescription(cat_name, info.cat25k, info.cat,
                            (termInfo.contexts[0].length * 1000) / numCatDocs));
                    d3.select("#" + divName + "-" + "notcathead").style("fill", color(0)).html(
                        getFrequencyDescription(ncat_name, info.ncat25k, info.ncat,
                            (termInfo.contexts[1].length * 1000) / numNCatDocs));
                    if (showNeutral) {
                        var numList = fullData.docs.categories.map(function (x, i) {
                            if (fullData.info.neutral_category_internal_names.indexOf(x) > -1) {
                                return i;
                            } else {
                                return -1;
                            }
                        }).filter(function (x) {
                            return x > -1;
                        });
                        var numDocs = fullData.docs.labels.map(function (x) {
                            return numList.indexOf(x) > -1;
                        }).reduce(function (a, b) {
                            return a + b;
                        }, 0);
                        d3.select("#" + divName + "-neuthead").style("fill", color(0)).html(
                            getFrequencyDescription(fullData.info.neutral_category_name, info.neut25k,
                                info.neut,
                                (termInfo.contexts[2].length * 1000) / numDocs));
                        if (showExtra) {
                            var numList = fullData.docs.categories.map(function (x, i) {
                                if (fullData.info.extra_category_internal_names.indexOf(x) > -1) {
                                    return i;
                                } else {
                                    return -1;
                                }
                            }).filter(function (x) {
                                return x > -1;
                            });
                            var numDocs = fullData.docs.labels.map(function (x) {
                                return numList.indexOf(x) > -1;
                            }).reduce(function (a, b) {
                                return a + b;
                            }, 0);
                            d3.select("#" + divName + "-extrahead").style("fill", color(0)).html(
                                getFrequencyDescription(fullData.info.extra_category_name, info
                                    .extra25k, info.extra,
                                    (termInfo.contexts[3].length * 1000) / numDocs));
                        }
                    }
                } else if (unifiedContexts && !ignoreCategories) {
                    // extra unified context code goes here
                    console.log("docLabelCountsSorted");
                    console.log(docLabelCountsSorted);
                    docLabelCountsSorted.forEach(function (counts) {
                        var htmlToAdd = (ignoreCategories ? "" : "<b>" + counts.label + "</b>: ") +
                            getCategoryStatsHTML(counts);
                        if (showCategoryHeadings) {
                            d3.select("#" + divName + "-" + "contexts").append("div").html(
                                htmlToAdd).on("click", function () {
                                window.location.hash = "#" + divName + "-" + "category" +
                                    counts.labelNum;
                            });
                        }
                    });
                }
                if (jump) {
                    if (window.location.hash === "#" + divName + "-" + "snippets") {
                        window.location.hash = "#" + divName + "-" + "snippetsalt";
                    } else {
                        window.location.hash = "#" + divName + "-" + "snippets";
                    }
                }
            }

            function searchInText(d, includeAll = true) {
                function stripNonWordChars(term) {
                    //d.term.replace(" ", "[^\\w]+")
                }

                function removeUnderScoreJoin(term) {
                    /*
                                    '_ _asjdklf_jaksdlf_jaksdfl skld_Jjskld asdfjkl_sjkdlf'
                                      ->
                                    "_ _asjdklf jaksdlf jaksdfl skld Jjskld asdfjkl_sjkdlf"
                                     */
                    return term.replace(/(\w+)(_)(\w+)/, "$1 $3").replace(/(\w+)(_)(\w+)/, "$1 $3").replace(
                        /(\w+)(_)(\w+)/, "$1 $3");
                }

                function buildMatcher(term) {
                    var boundary = "(?:\\W|^|$)";
                    var wordSep = "[^\\w]+";
                    if (asianMode) {
                        boundary = "( |$|^)";
                        wordSep = " ";
                    }
                    if (isEmoji(term)) {
                        boundary = "";
                        wordSep = "";
                    }
                    if (matchFullLine) {
                        boundary = "($|^)";
                    }
                    var termToRegex = term;
                    // https://stackoverflow.com/questions/3446170/escape-string-for-use-in-javascript-regex
                    function escapeRegExp(string) {
                        return string.replace(/[\-\[\]\/\{\}\(\)\*\+\?\.\,\\\^\$\|\'#?]/g, "\\$&");
                        //return string.replace(/[\?#.*+^${}()|[\]\\]'\%/g, '\\$&'); // $& means the whole matched string
                    }
                    /*
                                    ['[', ']', '(', ')', '{', '}', '^', '$', '|', '?', '"',
                                        '*', '+', '-', '=', '~', '`', '{'].forEach(function (a) {
                                        termToRegex = termToRegex.replace(a, '\\\\' + a)
                                    });
                                    ['.', '#'].forEach(function(a) {termToRegex = termToRegex.replace(a, '\\' + a)})
                                    */
                    termToRegex = escapeRegExp(termToRegex);
                    console.log("termToRegex");
                    console.log(termToRegex);
                    var regexp = new RegExp(boundary + "(" + removeUnderScoreJoin(termToRegex.replace(" ",
                        wordSep, "gim")) + ")" + boundary, "gim");
                    console.log(regexp);
                    if (subwordEncoding === "RoBERTa") {
                        if (term.charCodeAt(0) === 288 || term.charCodeAt(0) === 289) {
                            // Starts with character Ġ indicating it's a word start
                            console.log("START");
                            regexp = new RegExp(boundary + escapeRegExp(term.substr(1, term.length)),
                            "gim");
                        } else {
                            regexp = new RegExp("\w" + escapeRegExp(term), "gim");
                        }
                        console.log("SP");
                        console.log(regexp);
                    }
                    try {
                        regexp.exec("X");
                    } catch (err) {
                        console.log("Can't search " + term);
                        console.log(err);
                        return null;
                    }
                    return regexp;
                }
                var matches = [
                    [],
                    [],
                    [],
                    []
                ];
                var notmatches = [
                    [],
                    [],
                    [],
                    []
                ];
                var pattern = buildMatcher(d.term);
                var categoryNum = fullData.docs.categories.indexOf(fullData.info.category_internal_name);
                var notCategoryNumList = fullData.docs.categories.map(function (x, i) {
                    if (fullData.info.not_category_internal_names.indexOf(x) > -1) {
                        return i;
                    } else {
                        return -1;
                    }
                }).filter(function (x) {
                    return x > -1;
                });
                var neutralCategoryNumList = fullData.docs.categories.map(function (x, i) {
                    if (fullData.info.neutral_category_internal_names.indexOf(x) > -1) {
                        return i;
                    } else {
                        return -1;
                    }
                }).filter(function (x) {
                    return x > -1;
                });
                var extraCategoryNumList = fullData.docs.categories.map(function (x, i) {
                    if (fullData.info.extra_category_internal_names.indexOf(x) > -1) {
                        return i;
                    } else {
                        return -1;
                    }
                }).filter(function (x) {
                    return x > -1;
                });
                console.log("extraCategoryNumList");
                console.log(extraCategoryNumList);
                console.log("categoryNum");
                console.log(categoryNum);
                console.log("categoryNum");
                if (pattern !== null) {
                    for (var i in fullData.docs.texts) {
                        //var numericLabel = 1 * (fullData.docs.categories[fullData.docs.labels[i]] != fullData.info.category_internal_name);
                        var docLabel = fullData.docs.labels[i];
                        var numericLabel = -1;
                        if (docLabel == categoryNum) {
                            numericLabel = 0;
                        } else if (notCategoryNumList.indexOf(docLabel) > -1) {
                            numericLabel = 1;
                        } else if (neutralCategoryNumList.indexOf(docLabel) > -1) {
                            numericLabel = 2;
                        } else if (extraCategoryNumList.indexOf(docLabel) > -1) {
                            numericLabel = 3;
                        }
                        if (numericLabel == -1) {
                            continue;
                        }
                        var text = removeUnderScoreJoin(fullData.docs.texts[i]);
                        //var pattern = new RegExp("\\b(" + stripNonWordChars(d.term) + ")\\b", "gim");
                        var match;
                        var sentenceOffsets = null;
                        var lastSentenceStart = null;
                        var matchFound = false;
                        var curMatch = {
                            id: i,
                            snippets: [],
                            notsnippets: [],
                            docLabel: docLabel,
                        };
                        if (fullData.docs.meta) {
                            curMatch["meta"] = fullData.docs.meta[i];
                        }
                        while ((match = pattern.exec(text)) != null) {
                            if (sentenceOffsets == null) {
                                sentenceOffsets = getSentenceBoundaries(text);
                            }
                            var foundSnippet = getMatchingSnippet(text, sentenceOffsets, match.index,
                                pattern.lastIndex);
                            if (foundSnippet.sentenceStart == lastSentenceStart)
                        continue; // ensure we don't duplicate sentences
                            lastSentenceStart = foundSnippet.sentenceStart;
                            curMatch.snippets.push(foundSnippet.snippet);
                            matchFound = true;
                        }
                        if (matchFound) {
                            if (useFullDoc) {
                                curMatch.snippets = [
                                    text.replace(/\n$/g, "\n\n").replace(
                                        //new RegExp("\\b(" + d.term.replace(" ", "[^\\w]+") + ")\\b",
                                        //    'gim'),
                                        pattern, "<b>$&</b>"),
                                ];
                            }
                            matches[numericLabel].push(curMatch);
                        } else {
                            if (includeAll) {
                                curMatch.snippets = [text.replace(/\n$/g, "\n\n")];
                                notmatches[numericLabel].push(curMatch);
                            }
                        }
                    }
                }
                var toRet = {
                    contexts: matches,
                    notmatches: notmatches,
                    info: d,
                    docLabel: docLabel,
                };
                return toRet;
            }

            function getDefaultTooltipContent(d) {
                var term = formatTermForDisplay(d.term);
                var message = term + "<br/>" + d.cat25k + ":" + d.ncat25k + " per 25k words";
                message += "<br/>score: " + d.os.toFixed(5);
                return message;
            }

            function getDefaultTooltipContentWithoutScore(d) {
                var term = formatTermForDisplay(d.term);
                var message = term + "<br/>" + d.cat25k + ":" + d.ncat25k + " per 25k words";
                return message;
            }

            function getObscuredTerms(data, d) {
                //data = fullData['data']
                var matches = data.filter(function (term) {
                    return (term.x === d.x && term.y === d.y && (term.display === undefined || term
                        .display === true));
                }).map(function (term) {
                    return formatTermForDisplay(term.term);
                }).sort();
                return matches;
            }

            function showTooltip(data, d, pageX, pageY, showObscured = true) {
                deselectLastCircle();
                var obscuredTerms = getObscuredTerms(data, d);
                var message = "";
                console.log("!!!!! " + obscuredTerms.length);
                console.log(showObscured);
                if (obscuredTerms.length > 1 && showObscured) displayObscuredTerms(obscuredTerms, data, d
                    .term, d);
                if (getTooltipContent !== null) {
                    message += getTooltipContent(d);
                } else {
                    if (sortByDist) {
                        message += getDefaultTooltipContentWithoutScore(d);
                    } else {
                        message += getDefaultTooltipContent(d);
                    }
                }
                pageX -= svg.node().getBoundingClientRect().left - origSVGLeft;
                pageY -= svg.node().getBoundingClientRect().top - origSVGTop;
                tooltip.transition().duration(0).style("opacity", 1).style("z-index", 10000000);
                tooltip.html(message).style("left", pageX - 40 + "px").style("top", (pageY - 85 > 0 ?
                    pageY - 85 : 0) + "px");
                tooltip.on("click", function () {
                    tooltip.transition().style("opacity", 0);
                }).on("mouseout", function () {
                    tooltip.transition().style("opacity", 0);
                });
            }
            handleSearch = function (event) {
                var searchTerm = document.getElementById(this.divName + "-searchTerm").value;
                handleSearchTerm(searchTerm);
                return false;
            };

            function highlightTerm(searchTerm, showObscured) {
                deselectLastCircle();
                var cleanedTerm = searchTerm.toLowerCase().replace("'", " '").trim();
                if (this.termDict[cleanedTerm] === undefined) {
                    cleanedTerm = searchTerm.replace("'", " '").trim();
                }
                if (this.termDict[cleanedTerm] !== undefined) {
                    showToolTipForTerm(this.data, this.svg, cleanedTerm, this.termDict[cleanedTerm],
                        showObscured);
                }
                return cleanedTerm;
            }

            function handleSearchTerm(searchTerm, jump = false) {
                console.log("Handle search term.");
                console.log(searchTerm);
                console.log("this");
                console.log(this);
                highlighted = highlightTerm.call(this, searchTerm, true);
                console.log("found searchTerm");
                console.log(searchTerm);
                if (this.termDict[searchTerm] != null) {
                    var runDisplayTermContexts = true;
                    if (alternativeTermFunc != null) {
                        runDisplayTermContexts = this.alternativeTermFunc(this.termDict[searchTerm]);
                    }
                    if (runDisplayTermContexts) {
                        displayTermContexts(this.data, this.gatherTermContexts(this.termDict[searchTerm],
                            this.includeAllContexts), alwaysJump, this.includeAllContexts);
                    }
                }
            }

            function getCircleForSearchTerm(mysvg, searchTermInfo) {
                var circle = mysvg;
                if (circle.tagName !== "circle") {
                    // need to clean this thing up
                    circle = mysvg._groups[0][searchTermInfo.ci];
                    if (circle === undefined || circle.tagName != "circle") {
                        if (mysvg._groups[0].children !== undefined) {
                            circle = mysvg._groups[0].children[searchTermInfo.ci];
                        }
                    }
                    if (circle === undefined || circle.tagName != "circle") {
                        if (mysvg._groups[0][0].children !== undefined) {
                            circle = Array.prototype.filter.call(mysvg._groups[0][0].children,
                                (x) => x.tagName == "circle" && x.__data__["term"] == searchTermInfo
                                .term)[0];
                        }
                    }
                    if (
                        (circle === undefined || circle.tagName != "circle") && mysvg._groups[0][0]
                        .children !== undefined) {
                        circle = mysvg._groups[0][0].children[searchTermInfo.ci];
                    }
                }
                return circle;
            }

            function showToolTipForTerm(data, mysvg, searchTerm, searchTermInfo, showObscured = true) {
                //var searchTermInfo = termDict[searchTerm];
                console.log("showing tool tip");
                console.log(searchTerm);
                console.log(searchTermInfo);
                if (searchTermInfo === undefined) {
                    console.log("can't show");
                    d3.select("#" + divName + "-alertMessage").text(searchTerm +
                        " didn't make it into the visualization.");
                } else {
                    d3.select("#" + divName + "-alertMessage").text("");
                    var circle = getCircleForSearchTerm(mysvg, searchTermInfo);
                    if (circle) {
                        var mySVGMatrix = circle.getScreenCTM().translate(circle.cx.baseVal.value, circle.cy
                            .baseVal.value);
                        var pageX = mySVGMatrix.e;
                        var pageY = mySVGMatrix.f;
                        circle.style["stroke"] = "black";
                        //var circlePos = circle.position();
                        //var el = circle.node()
                        //showTooltip(searchTermInfo, pageX, pageY, circle.cx.baseVal.value, circle.cx.baseVal.value);
                        showTooltip(data, searchTermInfo, pageX, pageY, showObscured);
                        lastCircleSelected = circle;
                    }
                }
            }

            function makeWordInteractive(data, svg, domObj, term, termInfo, showObscured = true) {
                return domObj.on("mouseover", function (d) {
                    showToolTipForTerm(data, svg, term, termInfo, showObscured);
                    d3.select(this).style("stroke", "black");
                }).on("mouseout", function (d) {
                    tooltip.transition().duration(0).style("opacity", 0);
                    d3.select(this).style("stroke", null);
                    if (showObscured) {
                        d3.select("#" + divName + "-" + "overlapped-terms").selectAll("div")
                        .remove();
                    }
                }).on("click", function (d) {
                    var runDisplayTermContexts = true;
                    if (alternativeTermFunc != null) {
                        runDisplayTermContexts = alternativeTermFunc(termInfo);
                    }
                    if (runDisplayTermContexts) {
                        displayTermContexts(data, gatherTermContexts(termInfo, includeAllContexts),
                            alwaysJump, includeAllContexts);
                    }
                });
            }

            function processData(fullData) {
                modelInfo = fullData["info"];
                /*
                             categoryTermList.data(modelInfo['category_terms'])
                             .enter()
                             .append("li")
                             .text(function(d) {return d;});
                             */
                var data = fullData["data"];
                termDict = Object();
                data.forEach(function (x, i) {
                    termDict[x.term] = x;
                    //!!!
                    //termDict[x.term].i = i;
                });
                var padding = 0.1;
                if (showAxes || showAxesAndCrossHairs) {
                    padding = 0.1;
                }
                // Scale the range of the data.  Add some space on either end.
                if (useGlobalScale) {
                    var axisMax = Math.max(d3.max(data, function (d) {
                        return d.x;
                    }), d3.max(data, function (d) {
                        return d.y;
                    }));
                    var axisMin = Math.min(d3.min(data, function (d) {
                        return d.x;
                    }), d3.min(data, function (d) {
                        return d.y;
                    }));
                    axisMin = axisMin - (axisMax - axisMin) * padding;
                    axisMax = axisMax + (axisMax - axisMin) * padding;
                    x.domain([axisMin, axisMax]);
                    y.domain([axisMin, axisMax]);
                } else {
                    var xMax = d3.max(data, function (d) {
                        return d.x;
                    });
                    var yMax = d3.max(data, function (d) {
                        return d.y;
                    });
                    x.domain([-1 * padding, xMax + padding]);
                    y.domain([-1 * padding, yMax + padding]);
                }
                /*
                             data.sort(function (a, b) {
                             return Math.abs(b.os) - Math.abs(a.os)
                             });
                             */
                //var rangeTree = null; // keep boxes of all points and labels here
                var rectHolder = new RectangleHolder();
                var axisRectHolder = new RectangleHolder();
                // Add the scatterplot
                data.forEach(function (d, i) {
                    d.ci = i;
                });
                //console.log('XXXXX'); console.log(data)
                function getFilter(data) {
                    return data.filter(
                        (d) => d.display === undefined || d.display === true);
                }
                var mysvg = svg.selectAll("dot").data(getFilter(data))
                    //.filter(function (d) {return d.display === undefined || d.display === true})
                    .enter().append("circle").attr("r", function (d) {
                        if (pValueColors && d.p) {
                            return d.p >= 1 - minPVal || d.p <= minPVal ? 2 : 1.75;
                        }
                        return 2;
                    }).attr("cx", function (d) {
                        return x(d.x);
                    }).attr("cy", function (d) {
                        return y(d.y);
                    }).style("fill", function (d) {
                        //.attr("fill", function (d) {
                        if (colorFunc) {
                            return colorFunc(d);
                        } else if (greyZeroScores && d.os == 0) {
                            return d3.rgb(230, 230, 230);
                        } else if (pValueColors && d.p) {
                            if (d.p >= 1 - minPVal) {
                                return wordVecMaxPValue ? d3.interpolateYlGnBu(d.s) : color(d.s);
                            } else if (d.p <= minPVal) {
                                return wordVecMaxPValue ? d3.interpolateYlGnBu(d.s) : color(d.s);
                            } else {
                                return interpolateLightGreys(d.s);
                            }
                        } else {
                            if (d.term === "the") {
                                console.log("COLS " + d.s + " " + color(d.s) + " " + d.term);
                                console.log(d);
                                console.log(color);
                            }
                            return color(d.s);
                        }
                    }).on("mouseover", function (d) {
                        /*var mySVGMatrix = circle.getScreenCTM()n
                                                .translate(circle.cx.baseVal.value, circle.cy.baseVal.value);
                                            var pageX = mySVGMatrix.e;
                                            var pageY = mySVGMatrix.f;*/
                        /*showTooltip(
                                                d,
                                                d3.event.pageX,
                                                d3.event.pageY
                                            );*/
                        console.log("point MOUSOEVER");
                        console.log(d);
                        showToolTipForTerm(data, this, d.term, d, true);
                        d3.select(this).style("stroke", "black");
                    }).on("click", function (d) {
                        var runDisplayTermContexts = true;
                        if (alternativeTermFunc != null) {
                            runDisplayTermContexts = alternativeTermFunc(d);
                        }
                        if (runDisplayTermContexts) {
                            displayTermContexts(data, gatherTermContexts(d), alwaysJump,
                                includeAllContexts);
                        }
                    }).on("mouseout", function (d) {
                        tooltip.transition().duration(0).style("opacity", 0);
                        d3.select(this).style("stroke", null);
                        d3.select("#" + divName + "-" + "overlapped-terms").selectAll("div").remove();
                    });
                coords = Object();
                var pointStore = [];
                var pointRects = [];

                function censorPoints(datum, getX, getY) {
                    var term = datum.term;
                    var curLabel = svg.append("text").attr("x", x(getX(datum))).attr("y", y(getY(datum)) +
                        3).attr("text-anchor", "middle").text("x");
                    var bbox = curLabel.node().getBBox();
                    var borderToRemove = 0.5;
                    var x1 = bbox.x + borderToRemove,
                        y1 = bbox.y + borderToRemove,
                        x2 = bbox.x + bbox.width - borderToRemove,
                        y2 = bbox.y + bbox.height - borderToRemove;
                    //rangeTree = insertRangeTree(rangeTree, x1, y1, x2, y2, '~~' + term);
                    var pointRect = new Rectangle(x1, y1, x2, y2);
                    pointRects.push(pointRect);
                    rectHolder.add(pointRect);
                    pointStore.push([x1, y1]);
                    pointStore.push([x2, y1]);
                    pointStore.push([x1, y2]);
                    pointStore.push([x2, y2]);
                    curLabel.remove();
                }

                function censorCircle(xCoord, yCoord) {
                    var curLabel = svg.append("text").attr("x", x(xCoord)).attr("y", y(yCoord) + 3).attr(
                        "text-anchor", "middle").text("x");
                    var bbox = curLabel.node().getBBox();
                    var borderToRemove = 0.5;
                    var x1 = bbox.x + borderToRemove,
                        y1 = bbox.y + borderToRemove,
                        x2 = bbox.x + bbox.width - borderToRemove,
                        y2 = bbox.y + bbox.height - borderToRemove;
                    var pointRect = new Rectangle(x1, y1, x2, y2);
                    pointRects.push(pointRect);
                    rectHolder.add(pointRect);
                    pointStore.push([x1, y1]);
                    pointStore.push([x2, y1]);
                    pointStore.push([x1, y2]);
                    pointStore.push([x2, y2]);
                    curLabel.remove();
                }
                var configs = [{
                    anchor: "end",
                    group: 1,
                    xoff: -5,
                    yoff: -3,
                    "alignment-baseline": "ideographic",
                }, {
                    anchor: "end",
                    group: 1,
                    xoff: -5,
                    yoff: 10,
                    "alignment-baseline": "ideographic",
                }, {
                    anchor: "end",
                    group: 2,
                    xoff: 10,
                    yoff: 15,
                    "alignment-baseline": "ideographic",
                }, {
                    anchor: "end",
                    group: 2,
                    xoff: -10,
                    yoff: -15,
                    "alignment-baseline": "ideographic",
                }, {
                    anchor: "end",
                    group: 2,
                    xoff: 10,
                    yoff: -15,
                    "alignment-baseline": "ideographic",
                }, {
                    anchor: "end",
                    group: 2,
                    xoff: -10,
                    yoff: 15,
                    "alignment-baseline": "ideographic",
                }, {
                    anchor: "start",
                    group: 1,
                    xoff: 3,
                    yoff: 10,
                    "alignment-baseline": "ideographic",
                }, {
                    anchor: "start",
                    group: 1,
                    xoff: 3,
                    yoff: -3,
                    "alignment-baseline": "ideographic",
                }, {
                    anchor: "start",
                    group: 2,
                    xoff: 5,
                    yoff: 10,
                    "alignment-baseline": "ideographic",
                }, {
                    anchor: "start",
                    group: 2,
                    xoff: 5,
                    yoff: -3,
                    "alignment-baseline": "ideographic",
                }, {
                    anchor: "start",
                    group: 3,
                    xoff: 10,
                    yoff: 15,
                    "alignment-baseline": "ideographic",
                }, {
                    anchor: "start",
                    group: 3,
                    xoff: -10,
                    yoff: -15,
                    "alignment-baseline": "ideographic",
                }, {
                    anchor: "start",
                    group: 3,
                    xoff: 10,
                    yoff: -15,
                    "alignment-baseline": "ideographic",
                }, {
                    anchor: "start",
                    group: 3,
                    xoff: -10,
                    yoff: 15,
                    "alignment-baseline": "ideographic",
                }, ];
                if (centerLabelsOverPoints) {
                    configs = [{
                        anchor: "middle",
                        xoff: 0,
                        yoff: 0,
                        "alignment-baseline": "middle",
                    }, ];
                }

                function labelPointsIfPossible(datum, myX, myY) {
                    if (suppressTextColumn !== undefined && datum.etc !== undefined && datum.etc[
                            suppressTextColumn] === true) {
                        return false;
                    }
                    var term = datum.term;
                    if (datum.x > datum.y) {
                        configs.sort((a, b) => a.anchor == "end" && b.anchor == "end" ? a.group - b.group :
                            (a.anchor == "end") - (b.anchor == "end"));
                    } else {
                        configs.sort((a, b) => a.anchor == "start" && b.anchor == "start" ? a.group - b
                            .group : (a.anchor == "start") - (b.anchor == "start"));
                    }
                    var matchedElement = null;
                    var termColor = "rgb(0,0,0)";
                    if (textColorColumn !== undefined && datum.etc !== undefined && datum.etc[
                            textColorColumn] !== undefined) {
                        termColor = datum.etc[textColorColumn];
                    }
                    term = formatTermForDisplay(term);
                    for (var configI in configs) {
                        var config = configs[configI];
                        var curLabel = svg.append("text")
                            //.attr("x", x(data[i].x) + config['xoff'])
                            //.attr("y", y(data[i].y) + config['yoff'])
                            .attr("x", x(myX) + config["xoff"]).attr("y", y(myY) + config["yoff"]).attr(
                                "class", "label").attr("class", "pointlabel").attr("font-family",
                                "Helvetica, Arial, Sans-Serif").attr("font-size", "10px").attr(
                                "text-anchor", config["anchor"]).attr("alignment-baseline", config[
                                "alignment"]).attr("fill", termColor).text(term);
                        var bbox = curLabel.node().getBBox();
                        var borderToRemove = doCensorPoints ? 0.5 : 0.25;
                        var x1 = bbox.x + borderToRemove,
                            y1 = bbox.y + borderToRemove,
                            x2 = bbox.x + bbox.width - borderToRemove,
                            y2 = bbox.y + bbox.height - borderToRemove;
                        //matchedElement = searchRangeTree(rangeTree, x1, y1, x2, y2);
                        var matchedElement = false;
                        rectHolder.findMatchingRectangles(x1, y1, x2, y2, function (elem) {
                            matchedElement = true;
                            return false;
                        });
                        if (matchedElement) {
                            curLabel.remove();
                        } else {
                            curLabel = makeWordInteractive(data, svg, curLabel, term, datum);
                            break;
                        }
                    }
                    if (!matchedElement) {
                        coords[term] = [x1, y1, x2, y2];
                        //rangeTree = insertRangeTree(rangeTree, x1, y1, x2, y2, term);
                        var labelRect = new Rectangle(x1, y1, x2, y2);
                        rectHolder.add(labelRect);
                        pointStore.push([x1, y1]);
                        pointStore.push([x2, y1]);
                        pointStore.push([x1, y2]);
                        pointStore.push([x2, y2]);
                        return {
                            label: curLabel,
                            rect: labelRect,
                        };
                    } else {
                        //curLabel.remove();
                        return false;
                    }
                }
                var radius = 2;

                function euclideanDistanceSort(a, b) {
                    var aCatDist = a.x * a.x + (1 - a.y) * (1 - a.y);
                    var aNotCatDist = a.y * a.y + (1 - a.x) * (1 - a.x);
                    var bCatDist = b.x * b.x + (1 - b.y) * (1 - b.y);
                    var bNotCatDist = b.y * b.y + (1 - b.x) * (1 - b.x);
                    return (
                        (Math.min(aCatDist, aNotCatDist) > Math.min(bCatDist, bNotCatDist)) * 2 - 1);
                }

                function euclideanDistanceSortForCategory(a, b) {
                    var aCatDist = a.x * a.x + (1 - a.y) * (1 - a.y);
                    var bCatDist = b.x * b.x + (1 - b.y) * (1 - b.y);
                    return (aCatDist > bCatDist) * 2 - 1;
                }

                function euclideanDistanceSortForNotCategory(a, b) {
                    var aNotCatDist = a.y * a.y + (1 - a.x) * (1 - a.x);
                    var bNotCatDist = b.y * b.y + (1 - b.x) * (1 - b.x);
                    return (aNotCatDist > bNotCatDist) * 2 - 1;
                }

                function scoreSort(a, b) {
                    return a.s - b.s;
                }

                function scoreSortReverse(a, b) {
                    return b.s - a.s;
                }

                function backgroundScoreSort(a, b) {
                    if (b.bg === a.bg) return b.cat + b.ncat - (a.cat + a.ncat);
                    return b.bg - a.bg;
                }

                function arePointsPredictiveOfDifferentCategories(a, b) {
                    var aCatDist = a.x * a.x + (1 - a.y) * (1 - a.y);
                    var bCatDist = b.x * b.x + (1 - b.y) * (1 - b.y);
                    var aNotCatDist = a.y * a.y + (1 - a.x) * (1 - a.x);
                    var bNotCatDist = b.y * b.y + (1 - b.x) * (1 - b.x);
                    var aGood = aCatDist < aNotCatDist;
                    var bGood = bCatDist < bNotCatDist;
                    return {
                        aGood: aGood,
                        bGood: bGood,
                    };
                }

                function scoreSortForCategory(a, b) {
                    var __ret = arePointsPredictiveOfDifferentCategories(a, b);
                    if (sortByDist) {
                        var aGood = __ret.aGood;
                        var bGood = __ret.bGood;
                        if (aGood && !bGood) return -1;
                        if (!aGood && bGood) return 1;
                    }
                    return b.s - a.s;
                }

                function scoreSortForNotCategory(a, b) {
                    var __ret = arePointsPredictiveOfDifferentCategories(a, b);
                    if (sortByDist) {
                        var aGood = __ret.aGood;
                        var bGood = __ret.bGood;
                        if (aGood && !bGood) return 1;
                        if (!aGood && bGood) return -1;
                    }
                    if (reverseSortScoresForNotCategory) return a.s - b.s;
                    else return b.s - a.s;
                }
                var sortedData = data.map((x) => x).sort(sortByDist ? euclideanDistanceSort : scoreSort);
                if (doCensorPoints) {
                    for (var i in data) {
                        var d = sortedData[i];
                        if (!(censorPointColumn !== undefined && d.etc !== undefined && d.etc[
                                censorPointColumn] === false)) {
                            censorPoints(d, function (d) {
                                return d.x;
                            }, function (d) {
                                return d.y;
                            });
                        }
                    }
                }

                function registerFigureBBox(curLabel, axis = false) {
                    var bbox = curLabel.node().getBBox();
                    var borderToRemove = 1.5;
                    var x1 = bbox.x + borderToRemove,
                        y1 = bbox.y + borderToRemove,
                        x2 = bbox.x + bbox.width - borderToRemove,
                        y2 = bbox.y + bbox.height - borderToRemove;
                    var rect = new Rectangle(x1, y1, x2, y2);
                    if (axis) {
                        axisRectHolder.add(rect);
                    } else {
                        rectHolder.add(rect);
                    }
                    //return insertRangeTree(rangeTree, x1, y1, x2, y2, '~~_other_');
                }

                function drawXLabel(svg, labelText) {
                    return svg.append("text").attr("class", "x label").attr("text-anchor", "end").attr("x",
                            width).attr("y", height - 6).attr("font-family", "Helvetica, Arial, Sans-Serif")
                        .attr("font-size", "10px").text(labelText);
                }

                function drawYLabel(svg, labelText) {
                    return svg.append("text").attr("class", "y label").attr("text-anchor", "end").attr("y",
                        6).attr("dy", ".75em").attr("transform", "rotate(-90)").attr("font-family",
                        "Helvetica, Arial, Sans-Serif").attr("font-size", "10px").text(labelText);
                }
                d3.selection.prototype.moveToBack = function () {
                    return this.each(function () {
                        var firstChild = this.parentNode.firstChild;
                        if (firstChild) {
                            this.parentNode.insertBefore(this, firstChild);
                        }
                    });
                };
                if (verticalLines) {
                    if (typeof verticalLines === "number") {
                        verticalLines = [
                        verticalLines]; // r likes to make single element vectors doubles; this is a hackish workaround
                    }
                    for (i in verticalLines) {
                        svg.append("g").attr("transform", "translate(" + x(verticalLines[i]) + ", 1)")
                            .append("line").attr("y2", height).style("stroke", "#dddddd").style(
                                "stroke-width", "1px").moveToBack();
                    }
                }
                if (fullData["line"] !== undefined) {
                    var valueline = d3.line().x(function (d) {
                        return x(d.x);
                    }).y(function (d) {
                        return y(d.y);
                    });
                    fullData.line = fullData.line.sort((a, b) => b.x - a.x);
                    svg.append("path").attr("class", "line").style("stroke-width", "1px").attr("d",
                        valueline(fullData["line"])).moveToBack();
                }
                if (showAxes || showAxesAndCrossHairs) {
                    var myXAxis = svg.append("g").attr("class", "x axis").attr("transform", "translate(0," +
                        height + ")").call(xAxis);
                    //rangeTree = registerFigureBBox(myXAxis);
                    var xLabel = drawXLabel(svg, getLabelText("x"));
                    //console.log('xLabel');
                    //console.log(xLabel);
                    //rangeTree = registerFigureBBox(xLabel);
                    // Add the Y Axis
                    if (!yAxisValues) {
                        var myYAxis = svg.append("g").attr("class", "y axis").call(yAxis).selectAll("text")
                            .style("text-anchor", "end").attr("dx", "30px").attr("dy", "-13px").attr(
                                "font-family", "Helvetica, Arial, Sans-Serif").attr("font-size", "10px")
                            .attr("transform", "rotate(-90)");
                    } else {
                        var myYAxis = svg.append("g").attr("class", "y axis").call(yAxis).selectAll("text")
                            .style("text-anchor", "end").attr("font-family", "Helvetica, Arial, Sans-Serif")
                            .attr("font-size", "10px");
                    }
                    registerFigureBBox(myYAxis, true);
                    registerFigureBBox(myXAxis, true);

                    function getLabelText(axis) {
                        if (axis == "y") {
                            if (yLabelText == null) return modelInfo["category_name"] + " Frequency";
                            else return yLabelText;
                        } else {
                            if (xLabelText == null) return modelInfo["not_category_name"] + " Frequency";
                            else return xLabelText;
                        }
                    }
                    var yLabel = drawYLabel(svg, getLabelText("y"));
                }
                if (!showAxes || showAxesAndCrossHairs) {
                    horizontal_line_y_position_translated = 0.5;
                    if (horizontal_line_y_position !== null) {
                        var loOy = null,
                            hiOy = null,
                            loY = null,
                            hiY = null;
                        for (i in fullData.data) {
                            var curOy = fullData.data[i].oy;
                            if (curOy < horizontal_line_y_position && (curOy > loOy || loOy === null)) {
                                loOy = curOy;
                                loY = fullData.data[i].y;
                            }
                            if (curOy > horizontal_line_y_position && (curOy < hiOy || hiOy === null)) {
                                hiOy = curOy;
                                hiY = fullData.data[i].y;
                            }
                        }
                        horizontal_line_y_position_translated = loY + (hiY - loY) / 2;
                        if (loY === null) {
                            horizontal_line_y_position_translated = 0;
                        }
                    }
                    if (vertical_line_x_position === null) {
                        vertical_line_x_position_translated = 0.5;
                    } else {
                        if (vertical_line_x_position !== null) {
                            var loOx = null,
                                hiOx = null,
                                loX = null,
                                hiX = null;
                            for (i in fullData.data) {
                                var curOx = fullData.data[i].ox;
                                if (curOx < vertical_line_x_position && (curOx > loOx || loOx === null)) {
                                    loOx = curOx;
                                    loX = fullData.data[i].x;
                                }
                                if (curOx > vertical_line_x_position && (curOx < hiOx || hiOx === null)) {
                                    hiOx = curOx;
                                    hiX = fullData.data[i].x;
                                }
                            }
                            vertical_line_x_position_translated = loX + (hiX - loX) / 2;
                            if (loX === null) {
                                vertical_line_x_position_translated = 0;
                            }
                        }
                    }
                    if (showCrossAxes) {
                        var x_line = svg.append("g").attr("transform", "translate(0, " + y(
                            horizontal_line_y_position_translated) + ")").append("line").attr("x2",
                            width).style("stroke", "#cccccc").style("stroke-width", "1px").moveToBack();
                        var y_line = svg.append("g").attr("transform", "translate(" + x(
                            vertical_line_x_position_translated) + ", 0)").append("line").attr("y2",
                            height).style("stroke", "#cccccc").style("stroke-width", "1px").moveToBack();
                    }
                }
                if (showDiagonal) {
                    var diagonal = svg.append("g").append("line").attr("x1", 0).attr("y1", height).attr(
                        "x2", width).attr("y2", 0).style("stroke-dasharray", "5,5").style("stroke",
                        "#cccccc").style("stroke-width", "1px").moveToBack();
                }

                function showWordList(word, termDataList) {
                    var maxWidth = word.node().getBBox().width;
                    var wordObjList = [];
                    for (var i in termDataList) {
                        var datum = termDataList[i];
                        var curTerm = datum.term;
                        word = (function (word, curTerm) {
                            var termColor = "rgb(0,0,0)";
                            if (textColorColumn !== undefined && datum.etc !== undefined && datum
                                .etc[textColorColumn] !== undefined) {
                                termColor = datum.etc[textColorColumn];
                            }
                            var curWordPrinted = svg.append("text").attr("text-anchor", "start")
                                .attr("font-family", "Helvetica, Arial, Sans-Serif").attr(
                                    "font-size", "12px").attr("fill", termColor).attr("x", word
                                    .node().getBBox().x).attr("y", word.node().getBBox().y + 2 *
                                    word.node().getBBox().height).text(formatTermForDisplay(
                                    curTerm));
                            wordObjList.push(curWordPrinted);
                            return makeWordInteractive(termDataList, //data,
                                svg, curWordPrinted, curTerm, termDataList[i]);
                        })(word, curTerm);
                        if (word.node().getBBox().width > maxWidth) maxWidth = word.node().getBBox().width;
                        registerFigureBBox(word);
                    }
                    return {
                        word: word,
                        maxWidth: maxWidth,
                        wordObjList: wordObjList,
                    };
                }

                function pickEuclideanDistanceSortAlgo(category) {
                    if (category == true) return euclideanDistanceSortForCategory;
                    return euclideanDistanceSortForNotCategory;
                }

                function pickScoreSortAlgo(isTopPane) {
                    console.log("PICK SCORE ALGO");
                    console.log(isTopPane);
                    if (isTopPane === true) {
                        if (headerSortingAlgos !== null && headerSortingAlgos["upper"] !== undefined)
                        return headerSortingAlgos["upper"];
                        return scoreSortForCategory;
                    } else {
                        if (headerSortingAlgos !== null && headerSortingAlgos["lower"] !== undefined)
                        return headerSortingAlgos["lower"];
                        return scoreSortForNotCategory;
                    }
                }

                function pickTermSortingAlgorithm(isUpperPane) {
                    if (sortByDist) return pickEuclideanDistanceSortAlgo(isUpperPane);
                    return pickScoreSortAlgo(isUpperPane);
                }

                function showAssociatedWordList(data, word, header, isUpperPane, length = 14) {
                    var sortedData = null;
                    var sortingAlgo = pickTermSortingAlgorithm(isUpperPane);
                    console.log("showAssociatedWordList");
                    console.log(header);
                    console.log("WORD");
                    console.log(word);
                    sortedData = data.filter(
                        (term) => term.display === undefined || term.display === true).sort(sortingAlgo);
                    if (wordVecMaxPValue) {
                        function signifTest(x) {
                            if (isUpperPane) return x.p >= 1 - minPVal;
                            return x.p <= minPVal;
                        }
                        sortedData = sortedData.filter(signifTest);
                    }
                    return showWordList(word, sortedData.slice(0, length));
                }
                var characteristicXOffset = width;

                function showCatHeader(startingOffset, catName, registerFigureBBox) {
                    var catHeader = svg.append("text").attr("text-anchor", "start").attr("x",
                        startingOffset //width
                    ).attr("dy", "6px").attr("font-family", "Helvetica, Arial, Sans-Serif").attr(
                        "font-size", "12px").attr("font-weight", "bolder").attr("font-decoration",
                        "underline").text(catName
                        //"Top " + fullData['info']['category_name']
                    );
                    registerFigureBBox(catHeader);
                    return catHeader;
                }

                function showNotCatHeader(startingOffset, word, notCatName) {
                    console.log("showNotCatHeader");
                    console.log(word);
                    console.log(word.node().getBBox().y - word.node().getBBox().height);
                    console.log(word.node().getBBox().y + word.node().getBBox().height);
                    return svg.append("text").attr("font-family", "Helvetica, Arial, Sans-Serif").attr(
                        "font-size", "12px").attr("font-weight", "bolder").attr("font-decoration",
                        "underline").attr("text-anchor", "start").attr("x", startingOffset).attr("y",
                        word.node().getBBox().y + 3 * word.node().getBBox().height).text(notCatName);
                }

                function showTopTermsPane(data, registerFigureBBox, showAssociatedWordList, upperHeaderName,
                    lowerHeaderName, startingOffset) {
                    data = data.filter(
                        (term) => term.display === undefined || term.display === true);
                    //var catHeader = showCatHeader(startingOffset, catName, registerFigureBBox);
                    var catHeader = svg.append("text").attr("text-anchor", "start").attr("x",
                        startingOffset).attr("dy", "6px").attr("font-family",
                        "Helvetica, Arial, Sans-Serif").attr("font-size", "12px").attr("font-weight",
                        "bolder").attr("font-decoration", "underline").text(upperHeaderName
                        //"Top " + fullData['info']['category_name']
                    );
                    registerFigureBBox(catHeader);
                    var word = catHeader;
                    var wordListData = showAssociatedWordList(data, word, catHeader, true);
                    word = wordListData.word;
                    var maxWidth = wordListData.maxWidth;
                    var notCatHeader = showNotCatHeader(startingOffset, word, lowerHeaderName);
                    word = notCatHeader;
                    characteristicXOffset = catHeader.node().getBBox().x + maxWidth + 10;
                    var notWordListData = showAssociatedWordList(data, word, notCatHeader, false);
                    word = wordListData.word;
                    if (wordListData.maxWidth > maxWidth) {
                        maxWidth = wordListData.maxWidth;
                    }
                    return {
                        wordListData,
                        notWordListData,
                        word,
                        maxWidth,
                        characteristicXOffset,
                        startingOffset,
                        catHeader,
                        notCatHeader,
                        registerFigureBBox,
                    };
                }
                var payload = Object();
                if (showTopTerms) {
                    var upperHeaderName = "Top " + fullData["info"]["category_name"];
                    var lowerHeaderName = "Top " + fullData["info"]["not_category_name"];
                    if (headerNames !== null) {
                        if (headerNames.upper !== undefined) upperHeaderName = headerNames.upper;
                        if (headerNames.lower !== undefined) lowerHeaderName = headerNames.lower;
                    }
                    payload.topTermsPane = showTopTermsPane(data, registerFigureBBox,
                        showAssociatedWordList, upperHeaderName, lowerHeaderName, width);
                    payload.showTopTermsPane = showTopTermsPane;
                    payload.showAssociatedWordList = showAssociatedWordList;
                    payload.showWordList = showWordList;
                    /*var wordListData = topTermsPane.wordListData;
                                    var word = topTermsPane.word;
                                    var maxWidth = topTermsPane.maxWidth;
                                    var catHeader = topTermsPane.catHeader;
                                    var notCatHeader = topTermsPane.notCatHeader;
                                    var startingOffset = topTermsPane.startingOffset;*/
                    characteristicXOffset = payload.topTermsPane.characteristicXOffset;
                }
                if (
                    (!nonTextFeaturesMode && !asianMode && showCharacteristic) || (headerNames !== null &&
                        headerNames.right !== undefined)) {
                    var sortMethod = backgroundScoreSort;
                    var title = "Characteristic";
                    if (headerNames !== null && headerNames.right !== undefined) {
                        title = headerNames.right;
                    }
                    if (wordVecMaxPValue) {
                        title = "Most similar";
                        sortMethod = scoreSortReverse;
                    } else if (data.reduce(function (a, b) {
                            return a + b.bg;
                        }, 0) === 0) {
                        title = "Most frequent";
                    }
                    word = svg.append("text").attr("font-family", "Helvetica, Arial, Sans-Serif").attr(
                            "text-anchor", "start").attr("font-size", "12px").attr("font-weight", "bolder")
                        .attr("font-decoration", "underline").attr("x", characteristicXOffset).attr("dy",
                            "6px").text(title);
                    var rightSortMethod = sortMethod;
                    if (rightOrderColumn !== undefined && rightOrderColumn !== null) {
                        rightSortMethod = (a, b) => b.etc[rightOrderColumn] - a.etc[rightOrderColumn];
                    }
                    var wordListData = showWordList(word, data.filter(
                        (term) => term.display === undefined || term.display === true).sort(
                        rightSortMethod).slice(0, 30));
                    word = wordListData.word;
                    maxWidth = wordListData.maxWidth;
                    console.log(maxWidth);
                    console.log(word.node().getBBox().x + maxWidth);
                    svg.attr("width", word.node().getBBox().x + 3 * maxWidth + 10);
                }

                function performPartialLabeling(data, existingLabels, getX, getY, labelPriorityFunction = (
                        a, b) => Math.min(a.x, 1 - a.x, a.y, 1 - a.y) - Math.min(b.x, 1 - b.x, b.y, 1 - b
                    .y)) {
                    for (i in existingLabels) {
                        rectHolder.remove(existingLabels[i].rect);
                        existingLabels[i].label.remove();
                    }
                    var labeledPoints = [];
                    //var filteredData = data.filter(d=>d.display === undefined || d.display === true);
                    //for (var i = 0; i < filteredData.length; i++) {
                    data.sort(labelPriorityFunction).forEach(function (datum, i) {
                        //console.log(datum.i, datum.ci, i)
                        //var label = labelPointsIfPossible(i, getX(filteredData[i]), getY(filteredData[i]));
                        if (datum.display === undefined || datum.display === true) {
                            var label = labelPointsIfPossible(datum, getX(datum), getY(datum));
                            if (label !== false) {
                                //console.log("labeled")
                                labeledPoints.push(label);
                            }
                        }
                        //if (labelPointsIfPossible(i), true) numPointsLabeled++;
                    });
                    return labeledPoints;
                }
                //var labeledPoints = performPartialLabeling();
                var labeledPoints = [];
                var labelPriorityFunction = (a, b) => Math.min(a.x, 1 - a.x, a.y, 1 - a.y) - Math.min(b.x,
                    1 - b.x, b.y, 1 - b.y);
                if (labelPriorityColumn !== undefined && labelPriorityColumn !== null) {
                    labelPriorityFunction = (a, b) => b.etc[labelPriorityColumn] - a.etc[
                        labelPriorityColumn];
                }
                labeledPoints = performPartialLabeling(data, labeledPoints, function (d) {
                    return d.x;
                }, function (d) {
                    return d.y;
                }, labelPriorityFunction);
                if (backgroundLabels !== null) {
                    backgroundLabels.map(function (label) {
                        svg.append("text").attr("x", x(label.X)).attr("y", y(label.Y)).attr(
                            "text-anchor", "middle").style("font-size", "30").style("fill",
                            "rgb(200,200,200)").text(label.Text).lower().on("mouseover",
                            function (d) {
                                d3.select(this).style("stroke", "black").style("stroke-width",
                                    "1px").raise();
                            }).on("mouseout", function (d) {
                            d3.select(this).style("stroke-width", "0px").style("fill",
                                "rgb(200,200,200)").lower();
                        });
                    });
                }
                /*
                            // pointset has to be sorted by X
                            function convex(pointset) {
                                function _cross(o, a, b) {
                                    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0]);
                                }

                                function _upperTangent(pointset) {
                                    var lower = [];
                                    for (var l = 0; l < pointset.length; l++) {
                                        while (lower.length >= 2 && (_cross(lower[lower.length - 2], lower[lower.length - 1], pointset[l]) <= 0)) {
                                            lower.pop();
                                        }
                                        lower.push(pointset[l]);
                                    }
                                    lower.pop();
                                    return lower;
                                }

                                function _lowerTangent(pointset) {
                                    var reversed = pointset.reverse(),
                                        upper = [];
                                    for (var u = 0; u < reversed.length; u++) {
                                        while (upper.length >= 2 && (_cross(upper[upper.length - 2], upper[upper.length - 1], reversed[u]) <= 0)) {
                                            upper.pop();
                                        }
                                        upper.push(reversed[u]);
                                    }
                                    upper.pop();
                                    return upper;
                                }

                                var convex,
                                    upper = _upperTangent(pointset),
                                    lower = _lowerTangent(pointset);
                                convex = lower.concat(upper);
                                convex.push(pointset[0]);
                                return convex;
                            }

                            console.log("POINTSTORE")
                            console.log(pointStore);
                            pointStore.sort();
                            var convexHull = convex(pointStore);
                            var minX = convexHull.sort(function (a,b) {
                                return a[0] < b[0] ? -1 : 1;
                            })[0][0];
                            var minY = convexHull.sort(function (a,b) {
                                return a[1] < b[1] ? -1 : 1;
                            })[0][0];
                            //svg.append("text").text("BLAH BLAH").attr("text-anchor", "middle").attr("cx", x(0)).attr("y", minY);
                            console.log("POINTSTORE")
                            console.log(pointStore);
                            console.log(convexHull);
                            for (i in convexHull) {
                                var i = parseInt(i);
                                if (i + 1 == convexHull.length) {
                                    var nextI = 0;
                                } else {
                                    var nextI = i + 1;
                                }
                                console.log(i, ',', nextI);
                                svg.append("line")
                                    .attr("x2", width)
                                    .style("stroke", "#cc0000")
                                    .style("stroke-width", "1px")
                                    .attr("x1", convexHull[i][0])     // x position of the first end of the line
                                    .attr("y1", convexHull[i][1])      // y position of the first end of the line
                                    .attr("x2", convexHull[nextI][0])     // x position of the second end of the line
                                    .attr("y2", convexHull[nextI][1]);    // y position of the second end of the line
                            }*/
                function populateCorpusStats() {
                    var wordCounts = {};
                    var docCounts = {};
                    fullData.docs.labels.forEach(function (x, i) {
                        var cnt = (fullData.docs.texts[i].trim().replace(/['";:,.?¿\-!¡]+/g, "")
                            .match(/\S+/g) || []).length;
                        var name = null;
                        if (unifiedContexts) {
                            var name = fullData.docs.categories[x];
                            wordCounts[name] = wordCounts[name] ? wordCounts[name] + cnt : cnt;
                        } else {
                            if (fullData.docs.categories[x] == fullData.info
                                .category_internal_name) {
                                name = fullData.info.category_name;
                            } else if (fullData.info.not_category_internal_names.indexOf(fullData
                                    .docs.categories[x]) > -1) {
                                name = fullData.info.not_category_name;
                            } else if (fullData.info.neutral_category_internal_names.indexOf(
                                    fullData.docs.categories[x]) > -1) {
                                name = fullData.info.neutral_category_name;
                            } else if (fullData.info.extra_category_internal_names.indexOf(fullData
                                    .docs.categories[x]) > -1) {
                                name = fullData.info.extra_category_name;
                            }
                            if (name) {
                                wordCounts[name] = wordCounts[name] ? wordCounts[name] + cnt : cnt;
                            }
                        }
                        //!!!
                    });
                    fullData.docs.labels.forEach(function (x) {
                        if (unifiedContexts) {
                            var name = fullData.docs.categories[x];
                            docCounts[name] = docCounts[name] ? docCounts[name] + 1 : 1;
                        } else {
                            var name = null;
                            if (fullData.docs.categories[x] == fullData.info
                                .category_internal_name) {
                                name = fullData.info.category_name;
                            } else if (fullData.info.not_category_internal_names.indexOf(fullData
                                    .docs.categories[x]) > -1) {
                                name = fullData.info.not_category_name;
                            } else if (fullData.info.neutral_category_internal_names.indexOf(
                                    fullData.docs.categories[x]) > -1) {
                                name = fullData.info.neutral_category_name;
                            } else if (fullData.info.extra_category_internal_names.indexOf(fullData
                                    .docs.categories[x]) > -1) {
                                name = fullData.info.extra_category_name;
                            }
                            if (name) {
                                docCounts[name] = docCounts[name] ? docCounts[name] + 1 : 1;
                            }
                        }
                    });
                    console.log("docCounts");
                    console.log(docCounts);
                    var messages = [];
                    if (ignoreCategories) {
                        var wordCount = getCorpusWordCounts();
                        console.log("wordCount");
                        console.log(wordCount);
                        messages.push("<b>Document count: </b>" + fullData.docs.texts.length.toLocaleString(
                            "en") + "; <b>word count: </b>" + wordCount["sums"].reduce((a, b) => a +
                            b, 0).toLocaleString("en"));
                    } else if (unifiedContexts) {
                        fullData.docs.categories.forEach(function (x, i) {
                            if (docCounts[x] > 0) {
                                var message = "<b>" + x + "</b>: ";
                                message += "document count: " + Number(docCounts[x]).toLocaleString(
                                        "en") + "; word count: " + Number(wordCounts[x])
                                    .toLocaleString("en");
                                messages.push(message);
                            }
                        });
                    } else {
                        [
                            fullData.info.category_name,
                            fullData.info.not_category_name,
                            fullData.info.neutral_category_name,
                            fullData.info.extra_category_name,
                        ].forEach(function (x, i) {
                            if (docCounts[x] > 0) {
                                messages.push("<b>" + x + "</b> document count: " + Number(
                                        docCounts[x]).toLocaleString("en") + "; word count: " +
                                    Number(wordCounts[x]).toLocaleString("en"));
                            }
                        });
                    }
                    if (showCorpusStats) {
                        d3.select("#" + divName + "-" + "corpus-stats").style("width", width + margin.left +
                            margin.right + 200).append("div").html(messages.join("<br />"));
                    }
                }
                if (fullData.docs) {
                    populateCorpusStats();
                }
                if (saveSvgButton) {
                    // from https://stackoverflow.com/questions/23218174/how-do-i-save-export-an-svg-file-after-creating-an-svg-with-d3-js-ie-safari-an
                    var svgElement = document.getElementById(divName);
                    var serializer = new XMLSerializer();
                    var source = serializer.serializeToString(svgElement);
                    if (!source.match(/^<svg[^>]+xmlns="http\:\/\/www\.w3\.org\/2000\/svg"/)) {
                        source = source.replace(/^<svg/, '<svg xmlns="https://www.w3.org/2000/svg"');
                    }
                    if (!source.match(/^<svg[^>]+"http\:\/\/www\.w3\.org\/1999\/xlink"/)) {
                        source = source.replace(/^<svg/,
                        '<svg xmlns:xlink="https://www.w3.org/1999/xlink"');
                    }
                    source = '<?xml version="1.0" standalone="no"?>\r\n' + source;
                    var url = "data:image/svg+xml;charset=utf-8," + encodeURIComponent(source);
                    var downloadLink = document.createElement("a");
                    downloadLink.href = url;
                    downloadLink.download = fullData["info"]["category_name"] + ".svg";
                    downloadLink.innerText = "Download SVG";
                    document.body.appendChild(downloadLink);
                }

                function rerender(xCoords, yCoords, color) {
                    labeledPoints.forEach(function (p) {
                        p.label.remove();
                        rectHolder.remove(p.rect);
                    });
                    pointRects.forEach(function (rect) {
                        rectHolder.remove(rect);
                    });
                    pointRects = [];
                    /*
                                    var circles = d3.select('#' + divName).selectAll('circle')
                                        .attr("cy", function (d) {return y(yCoords[d.i])})
                                        .transition(0)
                                        .attr("cx", function (d) {return x(xCoords[d.i])})
                                        .transition(0);
                                    */
                    d3.select("#" + divName).selectAll("dot").remove();
                    d3.select("#" + divName).selectAll("circle").remove();
                    console.log(this.fullData);
                    console.log(this);
                    console.log("X/Y coords");
                    console.log(this.fullData.data.filter((d) => d.display === undefined || d.display ===
                        true).map((d) => [d.x, d.y]));
                    var circles = this.svg //.select('#' + divName)
                        .selectAll("dot").data(this.fullData.data.filter(
                            (d) => d.display === undefined || d.display === true))
                        //.filter(function (d) {return d.display === undefined || d.display === true})
                        .enter().append("circle").attr("cy", (d) => d.y).attr("cx", (d) => d.x).attr("r", (
                            d) => 2).on("mouseover", function (d) {
                            /*var mySVGMatrix = circle.getScreenCTM()n
                                                        .translate(circle.cx.baseVal.value, circle.cy.baseVal.value);
                                                    var pageX = mySVGMatrix.e;
                                                    var pageY = mySVGMatrix.f;*/
                            /*showTooltip(
                                                        d,
                                                        d3.event.pageX,
                                                        d3.event.pageY
                                                    );*/
                            console.log("point MOUSOEVER");
                            console.log(d);
                            showToolTipForTerm(data, this, d.term, d, true);
                            d3.select(this).style("stroke", "black");
                        }).on("click", function (d) {
                            var runDisplayTermContexts = true;
                            if (alternativeTermFunc != null) {
                                runDisplayTermContexts = alternativeTermFunc(d);
                            }
                            if (runDisplayTermContexts) {
                                displayTermContexts(data, gatherTermContexts(d), alwaysJump,
                                    includeAllContexts);
                            }
                        }).on("mouseout", function (d) {
                            tooltip.transition().duration(0).style("opacity", 0);
                            d3.select(this).style("stroke", null);
                            d3.select("#" + divName + "-" + "overlapped-terms").selectAll("div")
                            .remove();
                        });
                    if (color !== null) {
                        console.log("COLOR");
                        console.log(color);
                        circles.style("fill", (d) => color(d));
                    }
                    xCoords.forEach((xCoord, i) => censorCircle(xCoord, yCoords[i]));
                    labeledPoints = [];
                    labeledPoints = performPartialLabeling(this.fullData.data, labeledPoints,
                        (d) => d.ox, //function (d) {return xCoords[d.ci]},
                        (d) => d.oy //function (d) {return yCoords[d.ci]}
                    );
                }
                //return [performPartialLabeling, labeledPoints];
                return {
                    ...payload,
                    ...{
                        rerender: rerender,
                        performPartialLabeling: performPartialLabeling,
                        showToolTipForTerm: showToolTipForTerm,
                        svg: svg,
                        data: data,
                        xLabel: xLabel,
                        yLabel: yLabel,
                        drawXLabel: drawXLabel,
                        drawYLabel: drawYLabel,
                        populateCorpusStats: populateCorpusStats,
                    },
                };
            }
            //fullData = getDataAndInfo();
            if (fullData.docs) {
                var corpusWordCounts = getCorpusWordCounts();
            }
            var payload = processData(fullData);
            // The tool tip is down here in order to make sure it has the highest z-index
            var tooltip = d3.select("#" + divName).append("div")
                //.attr("class", getTooltipContent == null && sortByDist ? "tooltip" : "tooltipscore")
                .attr("class", "tooltipscore").style("opacity", 0);
            plotInterface = {};
            if (payload.topTermsPane) {
                plotInterface.topTermsPane = payload.topTermsPane;
                plotInterface.showTopTermsPane = payload.showTopTermsPane;
                plotInterface.showAssociatedWordList = payload.showAssociatedWordList;
            }
            plotInterface.includeAllContexts = includeAllContexts;
            plotInterface.divName = divName;
            plotInterface.displayTermContexts = displayTermContexts;
            plotInterface.gatherTermContexts = gatherTermContexts;
            plotInterface.xLabel = payload.xLabel;
            plotInterface.yLabel = payload.yLabel;
            plotInterface.drawXLabel = payload.drawXLabel;
            plotInterface.drawYLabel = payload.drawYLabel;
            plotInterface.svg = payload.svg;
            plotInterface.termDict = termDict;
            plotInterface.showToolTipForTerm = payload.showToolTipForTerm;
            plotInterface.fullData = fullData;
            plotInterface.data = payload.data;
            plotInterface.rerender = payload.rerender;
            plotInterface.populateCorpusStats = payload.populateCorpusStats;
            plotInterface.handleSearch = handleSearch;
            plotInterface.handleSearchTerm = handleSearchTerm;
            plotInterface.highlightTerm = highlightTerm;
            plotInterface.y = y;
            plotInterface.x = x;
            plotInterface.tooltip = tooltip;
            plotInterface.alternativeTermFunc = alternativeTermFunc;
            plotInterface.showTooltipSimple = function (term) {
                plotInterface.showToolTipForTerm(plotInterface.data, plotInterface.svg, term.replace(
                    "'", "\\'"), plotInterface.termDict[term.replace("'", "\\'")]);
            };
            plotInterface.drawCategoryAssociation = function (category, otherCategory = null) {
                console.log("+++++++ Entering drawCategoryAssociation");
                console.log("Category: " + category);
                console.log("Other Category: " + otherCategory);
                var categoryNum = this.fullData.info.categories.indexOf(category);
                var otherCategoryNum = null;
                if (otherCategory !== null) otherCategoryNum = this.fullData.info.categories.indexOf(
                    otherCategory);
                console.log("cat/other: " + category + "/" + otherCategory + " ::: " + categoryNum +
                    "/" + otherCategoryNum);
                console.log("Full Data");
                console.log(this.fullData);
                /*
                            var rawLogTermCounts = getTermCounts(this.fullData).map(Math.log);
                            var maxRawLogTermCounts = Math.max(...rawLogTermCounts);
                            var minRawLogTermCounts = Math.min(...rawLogTermCounts);
                            var logTermCounts = rawLogTermCounts.map(
                                x => (x - minRawLogTermCounts) / maxRawLogTermCounts
                            )
                            */
                //var rawScores = getCategoryDenseRankScores(this.fullData, categoryNum);
                //console.log("RAW SCORES")
                //console.log(rawScores);
                /*
                            function logOddsRatioUninformativeDirichletPrior(fgFreqs, bgFreqs, alpha) {
                                var fgVocabSize = fgFreqs.reduce((x,y) => x+y);
                                var fgL = fgFreqs.map(x => (x + alpha)/((1+alpha)*fgVocabSize - x - alpha))
                                var bgVocabSize = bgFreqs.reduce((x,y) => x+y);
                                var bgL = bgFreqs.map(x => (x + alpha)/((1+alpha)*bgVocabSize - x - alpha))
                                var pooledVar = fgFreqs.map(function(x, i) {
                                    return (
                                        1/(x + alpha)
                                        + 1/((1+alpha)*fgVocabSize - x - alpha)
                                        + 1/(bgFreqs[i] + alpha)
                                        + 1/((1+alpha)*bgVocabSize - bgFreqs[i] - alpha))
                                })
                                return pooledVar.map(function(x, i) {
                                    return (Math.log(fgL[i]) - Math.log(bgL[i]))/x;
                                })
                            }
                            var rawScores = logOddsRatioUninformativeDirichletPrior(
                                denseRanks.fgFreqs, denseRanks.bgFreqs, 0.01);
                            */
                var denseRanks = getDenseRanks(this.fullData, categoryNum);
                if (otherCategoryNum !== null) {
                    var otherDenseRanks = getDenseRanks(this.fullData, otherCategoryNum);
                    denseRanks.bg = otherDenseRanks.fg;
                    denseRanks.bgFreqs = otherDenseRanks.fgFreqs;
                }
                var rawScores = denseRanks.fg.map((x, i) => x - denseRanks.bg[i]);
                var minRawScores = Math.min(...rawScores);
                var maxRawScores = Math.max(...rawScores);
                var scores = rawScores.map(function (rawScore) {
                    if (rawScore == 0) {
                        return 0.5;
                    } else if (rawScore > 0) {
                        return rawScore / (2 * maxRawScores) + 0.5;
                    } else if (rawScore < 0) {
                        return 0.5 - rawScore / (2 * minRawScores);
                    }
                });
                var fgFreqSum = denseRanks.fgFreqs.reduce((a, b) => a + b, 0);
                var bgFreqSum = denseRanks.bgFreqs.reduce((a, b) => a + b, 0);
                //!!! OLD and good
                var ox = denseRanks.bg;
                var oy = denseRanks.fg;
                var oxmax = Math.max(...ox);
                var oxmin = Math.min(...ox);
                var ox = ox.map((x) => (x - oxmin) / (oxmax - oxmin));
                var oymax = Math.max(...oy);
                var oymin = Math.min(...oy);
                var oy = oy.map((x) => (x - oymin) / (oymax - oymin));
                //var ox = logTermCounts
                //var oy = scores;
                var xf = this.x;
                var yf = this.y;
                this.fullData.data = this.fullData.data.map(function (term, i) {
                    //term.ci = i;
                    term.s = scores[term.i];
                    term.os = rawScores[term.i];
                    term.cat = denseRanks.fgFreqs[term.i];
                    term.ncat = denseRanks.bgFreqs[term.i];
                    term.cat25k = parseInt(
                        (denseRanks.fgFreqs[term.i] * 25000) / fgFreqSum);
                    term.ncat25k = parseInt(
                        (denseRanks.bgFreqs[term.i] * 25000) / bgFreqSum);
                    term.x = xf(ox[term.i]); // logTermCounts[term.i];
                    term.y = yf(oy[term.i]); // scores[term.i];
                    term.ox = ox[term.i];
                    term.oy = oy[term.i];
                    term.display = false;
                    return term;
                });
                // Feature selection
                var targetTermsToShow = 1500;
                var sortedBg = denseRanks.bg.map((x, i) => [x, i]).sort((a, b) => b[0] - a[0]).map((
                    x) => x[1]).slice(0, parseInt(targetTermsToShow / 2));
                var sortedFg = denseRanks.fg.map((x, i) => [x, i]).sort((a, b) => b[0] - a[0]).map((
                    x) => x[1]).slice(0, parseInt(targetTermsToShow / 2));
                var sortedScores = denseRanks.fg.map((x, i) => [x, i]).sort((a, b) => b[0] - a[0]).map((
                    x) => x[1]);
                var myFullData = this.fullData;
                sortedBg.concat(
                    sortedFg) //.concat(sortedScores.slice(0, parseInt(targetTermsToShow/2))).concat(sortedScores.slice(-parseInt(targetTermsToShow/4)))
                    .forEach(function (i) {
                        myFullData.data[i].display = true;
                    });
                console.log("newly filtered");
                console.log(myFullData);
                // begin rescaling to ignore hidden terms
                /*
                            function scaleDenseRanks(ranks) {
                                var max = Math.max(...ranks);
                                return ranks.map(x=>x/max)
                            }
                            var filteredData = myFullData.data.filter(d=>d.display);
                            var catRanks = scaleDenseRanks(denseRank(filteredData.map(d=>d.cat)))
                            var ncatRanks = scaleDenseRanks(denseRank(filteredData.map(d=>d.ncat)))
                            var rawScores = catRanks.map((x,i) => x - ncatRanks[i]);
                            function stretch_0_1(scores) {
                                var max = 1.*Math.max(...rawScores);
                                var min = -1.*Math.min(...rawScores);
                                return scores.map(function(x, i) {
                                    if(x == 0) return 0.5;
                                    if(x > 0) return (x/max + 1)/2;
                                    return (x/min + 1)/2;
                                })
                            }
                            var scores = stretch_0_1(rawScores);
                            console.log(scores)
                            filteredData.forEach(function(d, i) {
                                d.x = xf(catRanks[i]);
                                d.y = yf(ncatRanks[i]);
                                d.ox = catRanks[i];
                                d.oy = ncatRanks[i];
                                d.s = scores[i];
                                d.os = rawScores[i];
                            });
                            console.log("rescaled");
                            */
                // end rescaling
                this.rerender(
                    //denseRanks.bg,
                    fullData.data.map((x) => x.ox), //ox
                    //denseRanks.fg,
                    fullData.data.map((x) => x.oy), //oy,
                    (d) => d3.interpolateRdYlBu(d.s));
                if (this.yLabel !== undefined) {
                    this.yLabel.remove();
                }
                if (this.xLabel !== undefined) {
                    this.xLabel.remove();
                }
                var leftName = this.fullData.info.categories[categoryNum];
                var bottomName = "Not " + this.fullData.info.categories[categoryNum];
                if (otherCategoryNum !== null) {
                    bottomName = this.fullData.info.categories[otherCategoryNum];
                }
                this.yLabel = this.drawYLabel(this.svg, leftName + " Frequncy Rank");
                this.xLabel = this.drawXLabel(this.svg, bottomName + " Frequency Rank");
                if (this.topTermsPane !== undefined) {
                    this.topTermsPane.catHeader.remove();
                    this.topTermsPane.notCatHeader.remove();
                    this.topTermsPane.wordListData.wordObjList.map((x) => x.remove());
                    this.topTermsPane.notWordListData.wordObjList.map((x) => x.remove());
                }
                this.showWordList = payload.showWordList;
                this.showAssociatedWordList = function (data, word, header, isUpperPane, length = 14) {
                    var sortedData = null;
                    if (!isUpperPane) {
                        sortedData = data.map((x) => x).sort((a, b) => scores[a.i] - scores[b.i]);
                    } else {
                        sortedData = data.map((x) => x).sort((a, b) => scores[b.i] - scores[a.i]);
                    }
                    console.log("sortedData");
                    console.log(isUpperPane);
                    console.log(sortedData.slice(0, length));
                    console.log(payload);
                    console.log(word);
                    return payload.showWordList(word, sortedData.slice(0, length));
                };
                if (this.topTermsPane !== undefined) this.topTermsPane = payload.showTopTermsPane(this
                    .data, this.topTermsPane.registerFigureBBox, this.showAssociatedWordList,
                    "Top " + leftName, "Top " + bottomName, this.topTermsPane.startingOffset);
                fullData.info.category_name = leftName;
                fullData.info.not_category_name = bottomName;
                fullData.info.category_internal_name = this.fullData.info.categories[categoryNum];
                if (otherCategoryNum === null) {
                    fullData.info.not_category_internal_names = this.fullData.info.categories.filter(
                        (x) => x !== this.fullData.info.categories[categoryNum]);
                } else {
                    fullData.info.not_category_internal_names = this.fullData.info.categories.filter(
                        (x) => x === this.fullData.info.categories[otherCategoryNum]);
                    fullData.info.neutral_category_internal_names = this.fullData.info.categories
                        .filter(
                            (x) => x !== this.fullData.info.categories[categoryNum] && x !== this
                            .fullData.info.categories[otherCategoryNum]);
                    fullData.info.neutral_category_name = "All Others";
                }
                console.log("fullData.info.not_category_internal_names");
                console.log(fullData.info.not_category_internal_names);
                ["snippets", "snippetsalt", "termstats", "overlapped-terms-clicked", "categoryinfo",
                    "cathead", "cat", "corpus-stats", "notcathead", "notcat", "neuthead", "neut",
                ].forEach(function (divSubName) {
                    var mydiv = "#" + divName + "-" + divSubName;
                    console.log("Clearing");
                    console.log(mydiv);
                    d3.select(mydiv).selectAll("*").remove();
                    d3.select(mydiv).html("");
                });
                this.populateCorpusStats();
                console.log(fullData);
            };
            plotInterface.yAxisLogCounts = function (categoryName) {
                var categoryNum = this.fullData.docs.categories.indexOf(categoryName);
                var denseRanks = getDenseRanks(this.fullData, categoryNum);
                console.log("denseRanks");
                console.log(denseRanks);
                var rawScores = denseRanks.fg.map((x, i) => x - denseRanks.bg[i]);
                var minRawScores = Math.min(...rawScores);
                var maxRawScores = Math.max(...rawScores);
                var scores = rawScores.map(function (rawScore) {
                    if (rawScore == 0) {
                        return 0.5;
                    } else if (rawScore > 0) {
                        return rawScore / (2 * maxRawScores) + 0.5;
                    } else if (rawScore < 0) {
                        return 0.5 - rawScore / (2 * minRawScores);
                    }
                });
                var fgFreqSum = denseRanks.fgFreqs.reduce((a, b) => a + b, 0);
                var bgFreqSum = denseRanks.bgFreqs.reduce((a, b) => a + b, 0);
                var oy = denseRanks.fgFreqs.map(
                    (count) => Math.log(count + 1) / Math.log(2));
                var oymax = Math.max(...oy);
                var oymin = Math.min(...oy);
                oy = oy.map((y) => (y - oymin) / (oymax - oymin));
                var xf = this.x;
                var yf = this.y;
                var ox = this.fullData.data.map((term) => term.ox);
                var oxmax = Math.max(...ox);
                var oxmin = Math.min(...ox);
                ox = ox.map((y) => (y - oxmin) / (oxmax - oxmin));
                this.fullData.data = this.fullData.data.map(function (term, i) {
                    term.s = 1; //scores[i];
                    term.os = rawScores[i];
                    term.cat = denseRanks.fgFreqs[i];
                    term.ncat = denseRanks.bgFreqs[i];
                    term.cat25k = parseInt((denseRanks.fgFreqs[i] * 25000) / fgFreqSum);
                    term.ncat25k = parseInt((denseRanks.bgFreqs[i] * 25000) / bgFreqSum);
                    //term.x = xf(term.ox) // scores[term.i];
                    //term.ox = term.ox;
                    term.y = yf(oy[i]); // scores[term.i];
                    term.oy = oy[i];
                    term.x = xf(ox[i]); // scores[term.i];
                    term.ox = ox[i];
                    term.display = true;
                    return term;
                });
                this.rerender(
                    //denseRanks.bg,
                    this.fullData.data.map((point) => point.ox), //ox
                    this.fullData.data.map((point) => point.oy), //oy,
                    (d) => d3.interpolateRdYlBu(d.s));
                if (this.yLabel !== undefined) {
                    this.yLabel.remove();
                    this.yLabel = this.drawYLabel(this.svg, this.fullData.info.categories[categoryNum] +
                        " log freq.");
                }
                if (this.topTermsPane !== undefined) {
                    this.topTermsPane.catHeader.remove();
                    this.topTermsPane.notCatHeader.remove();
                    this.topTermsPane.wordListData.wordObjList.map((x) => x.remove());
                    this.topTermsPane.notWordListData.wordObjList.map((x) => x.remove());
                }
                this.showWordList = payload.showWordList;
                this.showAssociatedWordList = function (data, word, header, isUpperPane, length = 14) {
                    var sortedData = null;
                    if (!isUpperPane) {
                        sortedData = data.map((x) => x).sort((a, b) => scores[a.i] - scores[b.i]);
                    } else {
                        sortedData = data.map((x) => x).sort((a, b) => scores[b.i] - scores[a.i]);
                    }
                    console.log("HEADERHEADER222");
                    console.log("sortedData");
                    console.log(isUpperPane);
                    console.log(sortedData.slice(0, length));
                    console.log(payload);
                    console.log(word);
                    return payload.showWordList(word, sortedData.slice(0, length));
                };
                var leftName = this.fullData.info.categories[categoryNum];
                var bottomName = "Not " + this.fullData.info.categories[categoryNum];
                if (this.topTermsPane !== undefined) this.topTermsPane = payload.showTopTermsPane(this
                    .data, this.topTermsPane.registerFigureBBox, this.showAssociatedWordList,
                    "Top " + leftName, "Top " + bottomName, this.topTermsPane.startingOffset);
                fullData.info.category_name = leftName;
                fullData.info.not_category_name = bottomName;
                fullData.info.category_internal_name = this.fullData.info.categories[categoryNum];
                fullData.info.not_category_internal_names = this.fullData.info.categories.filter(
                    (x) => x !== this.fullData.info.categories[categoryNum]);
                console.log("fullData.info.not_category_internal_names");
                console.log(fullData.info.not_category_internal_names);
                ["snippets", "snippetsalt", "termstats", "overlapped-terms-clicked", "categoryinfo",
                    "cathead", "cat", "corpus-stats", "notcathead", "notcat", "neuthead", "neut",
                ].forEach(function (divSubName) {
                    var mydiv = "#" + divName + "-" + divSubName;
                    console.log("Clearing");
                    console.log(mydiv);
                    d3.select(mydiv).selectAll("*").remove();
                    d3.select(mydiv).html("");
                });
                this.populateCorpusStats();
            };
            return plotInterface;
        };
    })(d3);
    // Adapted from https://www.w3schools.com/howto/howto_js_autocomplete.asp
    function autocomplete(inputField, autocompleteValues, myPlotInterface) {
        var currentFocus; // current position in autocomplete list.
        inputField.addEventListener("input", function (e) {
            var matchedCandidateListDiv,
                matchedCandidateDiv,
                i,
                userInput = this.value;
            closeAllLists();
            if (!userInput) {
                return false;
            }
            currentFocus = -1;
            matchedCandidateListDiv = document.createElement("div");
            matchedCandidateListDiv.setAttribute("id", this.id + "autocomplete-list");
            matchedCandidateListDiv.setAttribute("class", "autocomplete-items");
            this.parentNode.appendChild(matchedCandidateListDiv);
            autocompleteValues.map(function (candidate) {
                var candidatePrefix = candidate.substr(0, userInput.length);
                if (candidatePrefix.toLowerCase() === userInput.toLowerCase()) {
                    matchedCandidateDiv = document.createElement("div");
                    matchedCandidateDiv.innerHTML = "<strong>" + candidatePrefix + "</strong>";
                    matchedCandidateDiv.innerHTML += candidate.substr(userInput.length);
                    matchedCandidateDiv.innerHTML += '<input type=hidden value="' + encodeURIComponent(
                        candidate) + '">';
                    matchedCandidateDiv.addEventListener("click", function (e) {
                        console.log("CLICK");
                        console.log(this.getElementsByTagName("input")[0].value);
                        inputField.value = decodeURIComponent(this.getElementsByTagName(
                            "input")[0].value);
                        console.log(inputField.value);
                        closeAllLists();
                        myPlotInterface.handleSearchTerm(inputField.value);
                    });
                    matchedCandidateListDiv.appendChild(matchedCandidateDiv);
                }
            });
        });
        inputField.addEventListener("keydown", function (keyboardEvent) {
            var candidateDivList = document.getElementById(this.id + "autocomplete-list");
            if (!candidateDivList) return true;
            var selectedCandidate = Array.prototype.find.call(candidateDivList.children,
                (x) => x.className !== "");
            if (keyboardEvent.keyCode === 40 || keyboardEvent.keyCode === 9) {
                // down or tab
                keyboardEvent.preventDefault();
                currentFocus++;
                addActive(candidateDivList.getElementsByTagName("div"));
            } else if (keyboardEvent.keyCode === 38) {
                //up
                currentFocus--;
                addActive(candidateDivList.getElementsByTagName("div"));
            } else if (keyboardEvent.keyCode === 13) {
                // enter
                keyboardEvent.preventDefault();
                var selectedTerm = inputField.value;
                console.log("selected term");
                console.log(selectedTerm);
                console.log(myPlotInterface);
                //if (selectedCandidate)
                //    selectedTerm = selectedCandidate.children[1].value;
                myPlotInterface.handleSearchTerm(selectedTerm);
                closeAllLists(null);
            } else if (keyboardEvent.keyCode === 27) {
                // esc
                closeAllLists(null);
            }
        });

        function addActive(candidateDivList) {
            if (!candidateDivList) return false;
            removeActive(candidateDivList);
            if (currentFocus >= candidateDivList.length) currentFocus = 0;
            if (currentFocus < 0) currentFocus = candidateDivList.length - 1;
            candidateDivList[currentFocus].classList.add("autocomplete-active");
            var selectedCandidate = Array.prototype.find.call(candidateDivList,
                (x) => x.className !== "");
            if (selectedCandidate) {
                var candidateValue = decodeURIComponent(selectedCandidate.children[1].value);
                myPlotInterface.highlightTerm(candidateValue);
                inputField.value = candidateValue;
            }
        }

        function removeActive(candidateDivList) {
            Array.prototype.find.call(candidateDivList, (x) => x.classList.remove("autocomplete-active"));
        }

        function closeAllLists(elmnt) {
            /*close all autocomplete lists in the document,
                    except the one passed as an argument:*/
            var x = document.getElementsByClassName("autocomplete-items");
            for (var i = 0; i < x.length; i++) {
                if (elmnt != x[i] && elmnt != inputField) {
                    x[i].parentNode.removeChild(x[i]);
                }
            }
        }
        /*execute a function when someone clicks in the document:*/
        document.addEventListener("click", function (e) {
            closeAllLists(e.target);
        });
    }

    function getDataAndInfo() {
        return {
            info: {
                category_name: "_",
                not_category_name: "not _",
                category_terms: ["geli", "ben", "yeniyim", "sadece", "icin", "bilgim", "bir", "fikrim", "yok", "ama", ],
                not_category_terms: ["geli", "ben", "yeniyim", "sadece", "icin", "bilgim", "bir", "fikrim", "yok",
                    "ama",
                ],
                category_internal_name: "_",
                not_category_internal_names: [],
                categories: ["_"],
                neutral_category_internal_names: [],
                extra_category_internal_names: [],
                neutral_category_name: "Neutral",
                extra_category_name: "Extra",
            },
            data: [{
                x: 0.2601546327828081,
                y: 0.1716950415294258,
                ox: 17,
                oy: 0.05233220776327364,
                term: "geli",
                cat25k: 209,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 17,
                ncat: 0,
                etc: {
                    Frequency: 17.0,
                    Range: 17.0,
                    SD: 0.11496483041662335,
                    VC: 8.581786458746766,
                    "Juilland's D": 0.665983795504786,
                    "Rosengren's S": 0.05233220776327364,
                    DP: 0.9423929098966127,
                    "DP norm": 0.9423929098966127,
                    "KL-divergence": 4.4328592433366385,
                    DA: 0.012618296529968598,
                    X: 17.0,
                    Xpos: 0.2601546327828081,
                    Y: 0.05233220776327364,
                    Ypos: 0.1716950415294258,
                    Expected: 0.044595237512910474,
                    Residual: 0.0077369702503631635,
                    ColorScore: 0.5226201798881104,
                },
                s: NaN,
                os: 0,
                bg: 0.0166015625,
            }, {
                x: 0.2927656550592527,
                y: 0.1538151012478072,
                ox: 19,
                oy: 0.047285100500216705,
                term: "ben",
                cat25k: 234,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 19,
                ncat: 0,
                etc: {
                    Frequency: 19.0,
                    Range: 15.0,
                    SD: 0.14509452921164775,
                    VC: 9.690787240504262,
                    "Juilland's D": 0.7133179371329286,
                    "Rosengren's S": 0.047285100500216705,
                    DP: 0.951255539143293,
                    "DP norm": 0.951255539143293,
                    "KL-divergence": 4.452990988783039,
                    DA: 0.009214677071227029,
                    X: 19.0,
                    Xpos: 0.2927656550592527,
                    Y: 0.047285100500216705,
                    Ypos: 0.1538151012478072,
                    Expected: 0.050026137081742104,
                    Residual: -0.0027410365815253995,
                    ColorScore: 0.49198617306935033,
                },
                s: NaN,
                os: 0,
                bg: 1.5269396352543039e-6,
            }, {
                x: 0.0391510034100286,
                y: 0.07392770725946195,
                ox: 8,
                oy: 0.02473467583018711,
                term: "yeniyim",
                cat25k: 98,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 8,
                ncat: 0,
                etc: {
                    Frequency: 8.0,
                    Range: 8.0,
                    SD: 0.07914817670285086,
                    VC: 12.554879529489718,
                    "Juilland's D": 0.5837464461307291,
                    "Rosengren's S": 0.02473467583018711,
                    DP: 0.973904480551466,
                    "DP norm": 0.973904480551466,
                    "KL-divergence": 5.425554853539667,
                    DA: 0.0055205047318613865,
                    X: 8.0,
                    Xpos: 0.0391510034100286,
                    Y: 0.02473467583018711,
                    Ypos: 0.07392770725946195,
                    Expected: 0.020969598587433753,
                    Residual: 0.0037650772427533577,
                    ColorScore: 0.5110077616648085,
                },
                s: NaN,
                os: 0,
                bg: 0.00784698381559588,
            }, {
                x: 0.07368463583902007,
                y: 0.0853377263065568,
                ox: 9,
                oy: 0.027955469026203154,
                term: "sadece",
                cat25k: 111,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 9,
                ncat: 0,
                etc: {
                    Frequency: 9.0,
                    Range: 9.0,
                    SD: 0.08391602529219312,
                    VC: 11.83215956619923,
                    "Juilland's D": 0.516418671670311,
                    "Rosengren's S": 0.027955469026203154,
                    DP: 0.9689807976366411,
                    "DP norm": 0.9689807976366411,
                    "KL-divergence": 5.35471066276507,
                    DA: 0.006309148264984299,
                    X: 9.0,
                    Xpos: 0.07368463583902007,
                    Y: 0.027955469026203154,
                    Ypos: 0.0853377263065568,
                    Expected: 0.026809092001212464,
                    Residual: 0.0011463770249906906,
                    ColorScore: 0.5033516032356037,
                },
                s: NaN,
                os: 0,
                bg: 0.0008843905075418858,
            }, {
                x: 0.07368463583902007,
                y: 0.07415844983512643,
                ox: 9,
                oy: 0.024799809298822348,
                term: "icin",
                cat25k: 111,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 9,
                ncat: 0,
                etc: {
                    Frequency: 9.0,
                    Range: 7.0,
                    SD: 0.10096527897901948,
                    VC: 14.236104336041747,
                    "Juilland's D": 0.568599618210625,
                    "Rosengren's S": 0.024799809298822348,
                    DP: 0.9719350073855361,
                    "DP norm": 0.9719350073855361,
                    "KL-divergence": 5.486390478465905,
                    DA: 0.0038555906063793,
                    X: 9.0,
                    Xpos: 0.07368463583902007,
                    Y: 0.024799809298822348,
                    Ypos: 0.07415844983512643,
                    Expected: 0.026809092001212464,
                    Residual: -0.002009282702390116,
                    ColorScore: 0.494125564051122,
                },
                s: NaN,
                os: 0,
                bg: 0.00047395860761493495,
            }, {
                x: 0.15803215576067894,
                y: 0.10931645105394122,
                ox: 12,
                oy: 0.034724126746821175,
                term: "bilgim",
                cat25k: 148,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 12,
                ncat: 0,
                etc: {
                    Frequency: 12.0,
                    Range: 12.0,
                    SD: 0.09678245621966297,
                    VC: 10.23474474522936,
                    "Juilland's D": 0.6538555624649214,
                    "Rosengren's S": 0.034724126746821175,
                    DP: 0.960610536681447,
                    "DP norm": 0.960610536681447,
                    "KL-divergence": 5.052685924186228,
                    DA: 0.00867507886435337,
                    X: 12.0,
                    Xpos: 0.15803215576067894,
                    Y: 0.034724126746821175,
                    Ypos: 0.10931645105394122,
                    Expected: 0.02879902189510588,
                    Residual: 0.005925104851715296,
                    ColorScore: 0.5173229227029048,
                },
                s: NaN,
                os: 0,
                bg: 0.011747430249632894,
            }, {
                x: 0.8206648406998286,
                y: 1.0,
                ox: 115,
                oy: 0.28614417279655147,
                term: "bir",
                cat25k: 1416,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 115,
                ncat: 0,
                etc: {
                    Frequency: 115.0,
                    Range: 104.0,
                    SD: 0.33045853497468014,
                    VC: 3.646538094633644,
                    "Juilland's D": 0.8818635898610158,
                    "Rosengren's S": 0.28614417279655147,
                    DP: 0.6914520583135357,
                    "DP norm": 0.6914520583135357,
                    "KL-divergence": 1.9259883344902722,
                    DA: 0.07384446577972859,
                    X: 115.0,
                    Xpos: 0.8206648406998286,
                    Y: 0.28614417279655147,
                    Ypos: 1.0,
                    Expected: 0.11512497028282875,
                    Residual: 0.1710192025137227,
                    ColorScore: 1.0,
                },
                s: NaN,
                os: 0,
                bg: 0.00033938471027612635,
            }, {
                x: 0.488175277354385,
                y: 0.2198027712803907,
                ox: 37,
                oy: 0.06591194395986985,
                term: "fikrim",
                cat25k: 455,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 37,
                ncat: 0,
                etc: {
                    Frequency: 37.0,
                    Range: 37.0,
                    SD: 0.16824594036353058,
                    VC: 5.77038103571136,
                    "Juilland's D": 0.8167851310136314,
                    "Rosengren's S": 0.06591194395986985,
                    DP: 0.9281142294436331,
                    "DP norm": 0.9281142294436331,
                    "KL-divergence": 4.041875943292285,
                    DA: 0.02839116719242918,
                    X: 37.0,
                    Xpos: 0.488175277354385,
                    Y: 0.06591194395986985,
                    Ypos: 0.2198027712803907,
                    Expected: 0.07146581635466058,
                    Residual: -0.005553872394790729,
                    ColorScore: 0.4837624304371754,
                },
                s: NaN,
                os: 0,
                bg: 0.03578336557059961,
            }, {
                x: 1.0,
                y: 0.6110680788036031,
                ox: 212,
                oy: 0.17635738976556703,
                term: "yok",
                cat25k: 2610,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 212,
                ncat: 0,
                etc: {
                    Frequency: 212.0,
                    Range: 212.0,
                    SD: 0.37303003587611394,
                    VC: 2.2329014883339084,
                    "Juilland's D": 0.9314068167432787,
                    "Rosengren's S": 0.17635738976556703,
                    DP: 0.7969073697314296,
                    "DP norm": 0.7969073697314296,
                    "KL-divergence": 2.6901727984863197,
                    DA: 0.16640378548895896,
                    X: 212.0,
                    Xpos: 1.0,
                    Y: 0.17635738976556703,
                    Ypos: 0.6110680788036031,
                    Expected: 0.1277271974506799,
                    Residual: 0.04863019231488713,
                    ColorScore: 0.6421775788920108,
                },
                s: NaN,
                os: 0,
                bg: 0.0043212392988177745,
            }, {
                x: 0.40645734454461835,
                y: 0.32746917165103495,
                ox: 28,
                oy: 0.0963037608641197,
                term: "ama",
                cat25k: 345,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 28,
                ncat: 0,
                etc: {
                    Frequency: 28.0,
                    Range: 28.0,
                    SD: 0.14689373863520605,
                    VC: 6.6574340831455885,
                    "Juilland's D": 0.7806691831002579,
                    "Rosengren's S": 0.0963037608641197,
                    DP: 0.898572131954714,
                    "DP norm": 0.898572131954714,
                    "KL-divergence": 3.4594584983858874,
                    DA: 0.021293375394321856,
                    X: 28.0,
                    Xpos: 0.40645734454461835,
                    Y: 0.0963037608641197,
                    Ypos: 0.32746917165103495,
                    Expected: 0.0634949286128288,
                    Residual: 0.0328088322512909,
                    ColorScore: 0.5959214865028338,
                },
                s: NaN,
                os: 0,
                bg: 2.0506788662528933e-5,
            }, {
                x: 0.34878247686409763,
                y: 0.15226768809205954,
                ox: 23,
                oy: 0.046848300373688714,
                term: "para",
                cat25k: 283,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 23,
                ncat: 0,
                etc: {
                    Frequency: 23.0,
                    Range: 20.0,
                    SD: 0.15008045209919516,
                    VC: 8.280525813646898,
                    "Juilland's D": 0.737003153520697,
                    "Rosengren's S": 0.046848300373688714,
                    DP: 0.9487936976858823,
                    "DP norm": 0.9487936976858823,
                    "KL-divergence": 4.544918368925554,
                    DA: 0.013235495816760423,
                    X: 23.0,
                    Xpos: 0.34878247686409763,
                    Y: 0.046848300373688714,
                    Ypos: 0.15226768809205954,
                    Expected: 0.05544025656004424,
                    Residual: -0.008591956186355526,
                    ColorScore: 0.4748801419370842,
                },
                s: NaN,
                os: 0,
                bg: 2.574661690853095e-6,
            }, {
                x: 0.4362997249293987,
                y: 0.1646201286562278,
                ox: 31,
                oy: 0.050335118087055764,
                term: "kazanmak",
                cat25k: 382,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 31,
                ncat: 0,
                etc: {
                    Frequency: 31.0,
                    Range: 31.0,
                    SD: 0.15437591587105237,
                    VC: 6.319452814205337,
                    "Juilland's D": 0.8115226203197308,
                    "Rosengren's S": 0.050335118087055764,
                    DP: 0.9473165928114341,
                    "DP norm": 0.9473165928114341,
                    "KL-divergence": 4.373223781985225,
                    DA: 0.023659305993690927,
                    X: 31.0,
                    Xpos: 0.4362997249293987,
                    Y: 0.050335118087055764,
                    Ypos: 0.1646201286562278,
                    Expected: 0.07146581635466058,
                    Residual: -0.021130698267604817,
                    ColorScore: 0.4382212700181745,
                },
                s: NaN,
                os: 0,
                bg: 0.030067895247332686,
            }, {
                x: 0.15803215576067894,
                y: 0.05858263543528209,
                ox: 12,
                oy: 0.02040310524124232,
                term: "can",
                cat25k: 148,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 12,
                ncat: 0,
                etc: {
                    Frequency: 12.0,
                    Range: 10.0,
                    SD: 0.11188803372292418,
                    VC: 11.832159566199232,
                    "Juilland's D": 0.6143542680517773,
                    "Rosengren's S": 0.02040310524124232,
                    DP: 0.978335795174812,
                    "DP norm": 0.978335795174812,
                    "KL-divergence": 5.71917047240868,
                    DA: 0.006046267087276513,
                    X: 12.0,
                    Xpos: 0.15803215576067894,
                    Y: 0.02040310524124232,
                    Ypos: 0.05858263543528209,
                    Expected: 0.02879902189510588,
                    Residual: -0.00839591665386356,
                    ColorScore: 0.47545329258218866,
                },
                s: NaN,
                os: 0,
                bg: 1.9318607875809095e-8,
            }, {
                x: 0.6395283972017078,
                y: 0.5330674297259477,
                ox: 62,
                oy: 0.15433955098745272,
                term: "tfb",
                cat25k: 763,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 62,
                ncat: 0,
                etc: {
                    Frequency: 62.0,
                    Range: 58.0,
                    SD: 0.2297270165103426,
                    VC: 4.701993289542335,
                    "Juilland's D": 0.8281395638820748,
                    "Rosengren's S": 0.15433955098745272,
                    DP: 0.8281634662727818,
                    "DP norm": 0.8281634662727818,
                    "KL-divergence": 2.8736862927560622,
                    DA: 0.042205149079067916,
                    X: 62.0,
                    Xpos: 0.6395283972017078,
                    Y: 0.15433955098745272,
                    Ypos: 0.5330674297259477,
                    Expected: 0.09614092908958558,
                    Residual: 0.05819862189786715,
                    ColorScore: 0.6701523017369855,
                },
                s: NaN,
                os: 0,
                bg: 0.0025466195678961632,
            }, {
                x: 0.40645734454461835,
                y: 0.10114407615332693,
                ox: 28,
                oy: 0.032417248084607844,
                term: "and",
                cat25k: 345,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 28,
                ncat: 0,
                etc: {
                    Frequency: 28.0,
                    Range: 16.0,
                    SD: 0.2234872810172189,
                    VC: 10.12876284324467,
                    "Juilland's D": 0.7083839118586597,
                    "Rosengren's S": 0.032417248084607844,
                    DP: 0.964549483013315,
                    "DP norm": 0.964549483013315,
                    "KL-divergence": 5.073144067928959,
                    DA: 0.008280757097791858,
                    X: 28.0,
                    Xpos: 0.40645734454461835,
                    Y: 0.032417248084607844,
                    Ypos: 0.10114407615332693,
                    Expected: 0.0634949286128288,
                    Residual: -0.03107768052822095,
                    ColorScore: 0.40913979228231034,
                },
                s: NaN,
                os: 0,
                bg: 4.308474453230597e-9,
            }, {
                x: 0.0,
                y: 0.04880172910781974,
                ox: 7,
                oy: 0.017642174131457546,
                term: "this",
                cat25k: 86,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 7,
                ncat: 0,
                etc: {
                    Frequency: 7.0,
                    Range: 7.0,
                    SD: 0.07406569038618868,
                    VC: 13.427051585724776,
                    "Juilland's D": 0.5966671978570424,
                    "Rosengren's S": 0.017642174131457546,
                    DP: 0.9817823732151808,
                    "DP norm": 0.9817823732151808,
                    "KL-divergence": 5.873876041532516,
                    DA: 0.004731861198738252,
                    X: 7.0,
                    Xpos: 0.0,
                    Y: 0.017642174131457546,
                    Ypos: 0.04880172910781974,
                    Expected: 0.022260856221882664,
                    Residual: -0.004618682090425118,
                    ColorScore: 0.48649659797690115,
                },
                s: NaN,
                os: 0,
                bg: 4.33641698867317e-9,
            }, {
                x: 0.0,
                y: 0.034743705944715216,
                ox: 7,
                oy: 0.013673908595153174,
                term: "will",
                cat25k: 86,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 7,
                ncat: 0,
                etc: {
                    Frequency: 7.0,
                    Range: 7.0,
                    SD: 0.07406569038618868,
                    VC: 13.427051585724776,
                    "Juilland's D": 0.5951276697538568,
                    "Rosengren's S": 0.013673908595153174,
                    DP: 0.9857213195470412,
                    "DP norm": 0.9857213195470412,
                    "KL-divergence": 6.253212017048595,
                    DA: 0.004731861198738252,
                    X: 7.0,
                    Xpos: 0.0,
                    Y: 0.013673908595153174,
                    Ypos: 0.034743705944715216,
                    Expected: 0.022260856221882664,
                    Residual: -0.00858694762672949,
                    ColorScore: 0.47489478520389994,
                },
                s: NaN,
                os: 0,
                bg: 1.0322232988548804e-8,
            }, {
                x: 0.0391510034100286,
                y: 0.019242531951171003,
                ox: 8,
                oy: 0.009298273854965787,
                term: "have",
                cat25k: 98,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 8,
                ncat: 0,
                etc: {
                    Frequency: 8.0,
                    Range: 7.0,
                    SD: 0.08854647369952867,
                    VC: 14.045684390587734,
                    "Juilland's D": 0.5616212632915378,
                    "Rosengren's S": 0.009298273854965787,
                    DP: 0.989660265878894,
                    "DP norm": 0.989660265878894,
                    "KL-divergence": 6.89645359608823,
                    DA: 0.004140378548895929,
                    X: 8.0,
                    Xpos: 0.0391510034100286,
                    Y: 0.009298273854965787,
                    Ypos: 0.019242531951171003,
                    Expected: 0.020969598587433753,
                    Residual: -0.011671324732467967,
                    ColorScore: 0.4658771513347121,
                },
                s: NaN,
                os: 0,
                bg: 1.0228839671453021e-8,
            }, {
                x: 0.0,
                y: 0.030564542065136802,
                ox: 7,
                oy: 0.012494224097447685,
                term: "about",
                cat25k: 86,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 7,
                ncat: 0,
                etc: {
                    Frequency: 7.0,
                    Range: 7.0,
                    SD: 0.07406569038618868,
                    VC: 13.427051585724776,
                    "Juilland's D": 0.6028397331019584,
                    "Rosengren's S": 0.012494224097447685,
                    DP: 0.9871984244214798,
                    "DP norm": 0.9871984244214798,
                    "KL-divergence": 6.358492816215196,
                    DA: 0.004731861198738252,
                    X: 7.0,
                    Xpos: 0.0,
                    Y: 0.012494224097447685,
                    Ypos: 0.030564542065136802,
                    Expected: 0.022260856221882664,
                    Residual: -0.009766632124434979,
                    ColorScore: 0.47144580263245206,
                },
                s: NaN,
                os: 0,
                bg: 1.1412398020319357e-8,
            }, {
                x: 0.47188236383573096,
                y: 0.23106104478644005,
                ox: 35,
                oy: 0.06908990278338328,
                term: "iyi",
                cat25k: 431,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 35,
                ncat: 0,
                etc: {
                    Frequency: 35.0,
                    Range: 34.0,
                    SD: 0.1685114755508105,
                    VC: 6.109744642113672,
                    "Juilland's D": 0.7826909426755111,
                    "Rosengren's S": 0.06908990278338328,
                    DP: 0.9226981782373307,
                    "DP norm": 0.9226981782373307,
                    "KL-divergence": 4.0401954751983045,
                    DA: 0.02528165840468688,
                    X: 35.0,
                    Xpos: 0.47188236383573096,
                    Y: 0.06908990278338328,
                    Ypos: 0.23106104478644005,
                    Expected: 0.07146581635466058,
                    Residual: -0.0023759135712772966,
                    ColorScore: 0.49305366433606584,
                },
                s: NaN,
                os: 0,
                bg: 0.0016126802746164125,
            }, {
                x: 0.18150043733463328,
                y: 0.1350126101942607,
                ox: 13,
                oy: 0.04197757778676127,
                term: "yerlere",
                cat25k: 160,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 13,
                ncat: 0,
                etc: {
                    Frequency: 13.0,
                    Range: 13.0,
                    SD: 0.10069429689496162,
                    VC: 9.829312519977409,
                    "Juilland's D": 0.6899959661169415,
                    "Rosengren's S": 0.04197757778676127,
                    DP: 0.9556868537666283,
                    "DP norm": 0.9556868537666283,
                    "KL-divergence": 4.6591865981297556,
                    DA: 0.009463722397476282,
                    X: 13.0,
                    Xpos: 0.18150043733463328,
                    Y: 0.04197757778676127,
                    Ypos: 0.1350126101942607,
                    Expected: 0.03413316267301318,
                    Residual: 0.007844415113748088,
                    ColorScore: 0.5229343108798518,
                },
                s: NaN,
                os: 0,
                bg: 0.012720156555772993,
            }, {
                x: 0.10457602270114133,
                y: 0.08339592687689149,
                ox: 10,
                oy: 0.02740734247485561,
                term: "gelece",
                cat25k: 123,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 10,
                ncat: 0,
                etc: {
                    Frequency: 10.0,
                    Range: 10.0,
                    SD: 0.08842014911062773,
                    VC: 11.22051692213866,
                    "Juilland's D": 0.6424722604619937,
                    "Rosengren's S": 0.02740734247485561,
                    DP: 0.9694731659281268,
                    "DP norm": 0.9694731659281268,
                    "KL-divergence": 5.338725148423357,
                    DA: 0.007097791798107211,
                    X: 10.0,
                    Xpos: 0.10457602270114133,
                    Y: 0.02740734247485561,
                    Ypos: 0.08339592687689149,
                    Expected: 0.025393729342041836,
                    Residual: 0.0020136131328137748,
                    ColorScore: 0.5058870966044068,
                },
                s: NaN,
                os: 0,
                bg: 0.009799118079372858,
            }, {
                x: 0.1325206812656045,
                y: 0.06396022164469906,
                ox: 11,
                oy: 0.02192107756037616,
                term: "with",
                cat25k: 135,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 11,
                ncat: 0,
                etc: {
                    Frequency: 11.0,
                    Range: 9.0,
                    SD: 0.10837523950411311,
                    VC: 12.502561720974503,
                    "Juilland's D": 0.566595696491756,
                    "Rosengren's S": 0.02192107756037616,
                    DP: 0.976366322008886,
                    "DP norm": 0.976366322008886,
                    "KL-divergence": 5.63678719481584,
                    DA: 0.005305420131918592,
                    X: 11.0,
                    Xpos: 0.1325206812656045,
                    Y: 0.02192107756037616,
                    Ypos: 0.06396022164469906,
                    Expected: 0.021504079936589475,
                    Residual: 0.0004169976237866843,
                    ColorScore: 0.5012191543921894,
                },
                s: NaN,
                os: 0,
                bg: 6.9114737541353615e-9,
            }, {
                x: 0.0,
                y: 0.058436623969323226,
                ox: 7,
                oy: 0.020361889469896137,
                term: "contribute",
                cat25k: 86,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 7,
                ncat: 0,
                etc: {
                    Frequency: 7.0,
                    Range: 7.0,
                    SD: 0.07406569038618868,
                    VC: 13.427051585724776,
                    "Juilland's D": 0.5915557841092649,
                    "Rosengren's S": 0.020361889469896137,
                    DP: 0.9788281634662958,
                    "DP norm": 0.9788281634662958,
                    "KL-divergence": 5.677533825135159,
                    DA: 0.004731861198738252,
                    X: 7.0,
                    Xpos: 0.0,
                    Y: 0.020361889469896137,
                    Ypos: 0.058436623969323226,
                    Expected: 0.022260856221882664,
                    Residual: -0.001898966751986527,
                    ColorScore: 0.494448089091533,
                },
                s: NaN,
                os: 0,
                bg: 6.290112101029983e-7,
            }, {
                x: 0.1325206812656045,
                y: 0.047850908594111216,
                ox: 11,
                oy: 0.017373778765196995,
                term: "the",
                cat25k: 135,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 11,
                ncat: 0,
                etc: {
                    Frequency: 11.0,
                    Range: 8.0,
                    SD: 0.1220544173557234,
                    VC: 14.08064142040118,
                    "Juilland's D": 0.581821571752247,
                    "Rosengren's S": 0.017373778765196995,
                    DP: 0.981782373215188,
                    "DP norm": 0.981782373215188,
                    "KL-divergence": 5.921267469083565,
                    DA: 0.004158302265557801,
                    X: 11.0,
                    Xpos: 0.1325206812656045,
                    Y: 0.017373778765196995,
                    Ypos: 0.047850908594111216,
                    Expected: 0.021504079936589475,
                    Residual: -0.0041303011713924795,
                    ColorScore: 0.487924452018594,
                },
                s: NaN,
                os: 0,
                bg: 9.509050652256204e-10,
            }, {
                x: 0.15803215576067894,
                y: 0.07435021893721798,
                ox: 12,
                oy: 0.024853941427495686,
                term: "twitter",
                cat25k: 148,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 12,
                ncat: 0,
                etc: {
                    Frequency: 12.0,
                    Range: 12.0,
                    SD: 0.09678245621966297,
                    VC: 10.23474474522936,
                    "Juilland's D": 0.6406228501211881,
                    "Rosengren's S": 0.024853941427495686,
                    DP: 0.9665189561792332,
                    "DP norm": 0.9665189561792332,
                    "KL-divergence": 5.78058427192253,
                    DA: 0.00867507886435337,
                    X: 12.0,
                    Xpos: 0.15803215576067894,
                    Y: 0.024853941427495686,
                    Ypos: 0.07435021893721798,
                    Expected: 0.02879902189510588,
                    Residual: -0.003945080467610194,
                    ColorScore: 0.48846597221357746,
                },
                s: NaN,
                os: 0,
                bg: 0.0007345514645119823,
            }, {
                x: 0.20322867227230915,
                y: 0.049007734593176346,
                ox: 14,
                oy: 0.01770032487273501,
                term: "instagram",
                cat25k: 172,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 14,
                ncat: 0,
                etc: {
                    Frequency: 14.0,
                    Range: 14.0,
                    SD: 0.10445380349648221,
                    VC: 9.46799118835971,
                    "Juilland's D": 0.6919871562094344,
                    "Rosengren's S": 0.01770032487273501,
                    DP: 0.9788281634662865,
                    "DP norm": 0.9788281634662865,
                    "KL-divergence": 6.055270494941157,
                    DA: 0.010252365930599416,
                    X: 14.0,
                    Xpos: 0.20322867227230915,
                    Y: 0.01770032487273501,
                    Ypos: 0.049007734593176346,
                    Expected: 0.03618450883181766,
                    Residual: -0.01848418395908265,
                    ColorScore: 0.4459587470664311,
                },
                s: NaN,
                os: 0,
                bg: 0.013691931540342298,
            }, {
                x: 0.1325206812656045,
                y: 0.019175872454732155,
                ox: 11,
                oy: 0.009279457369936801,
                term: "whatsapp",
                cat25k: 135,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 11,
                ncat: 0,
                etc: {
                    Frequency: 11.0,
                    Range: 11.0,
                    SD: 0.09269899826374953,
                    VC: 10.694093526972559,
                    "Juilland's D": 0.6776178487974591,
                    "Rosengren's S": 0.009279457369936801,
                    DP: 0.9881831610044433,
                    "DP norm": 0.9881831610044433,
                    "KL-divergence": 7.015465070224791,
                    DA: 0.007886435331230235,
                    X: 11.0,
                    Xpos: 0.1325206812656045,
                    Y: 0.009279457369936801,
                    Ypos: 0.019175872454732155,
                    Expected: 0.021504079936589475,
                    Residual: -0.012224622566652674,
                    ColorScore: 0.464259503064658,
                },
                s: NaN,
                os: 0,
                bg: 0.010773751224289911,
            }, {
                x: 0.0,
                y: 0.06846828733452123,
                ox: 7,
                oy: 0.02319360368334258,
                term: "olmas",
                cat25k: 86,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 7,
                ncat: 0,
                etc: {
                    Frequency: 7.0,
                    Range: 7.0,
                    SD: 0.07406569038618868,
                    VC: 13.427051585724776,
                    "Juilland's D": 0.5492822300178947,
                    "Rosengren's S": 0.02319360368334258,
                    DP: 0.9739044805514657,
                    "DP norm": 0.9739044805514657,
                    "KL-divergence": 5.600375501572746,
                    DA: 0.004731861198738252,
                    X: 7.0,
                    Xpos: 0.0,
                    Y: 0.02319360368334258,
                    Ypos: 0.06846828733452123,
                    Expected: 0.022260856221882664,
                    Residual: 0.0009327474614599165,
                    ColorScore: 0.5027270255262273,
                },
                s: NaN,
                os: 0,
                bg: 0.006869479882237487,
            }, {
                x: 0.33574935353791374,
                y: 0.18027382490427576,
                ox: 22,
                oy: 0.0547538064485841,
                term: "faydal",
                cat25k: 271,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 22,
                ncat: 0,
                etc: {
                    Frequency: 22.0,
                    Range: 21.0,
                    SD: 0.1364257154060566,
                    VC: 7.869283311376629,
                    "Juilland's D": 0.7450460925501485,
                    "Rosengren's S": 0.0547538064485841,
                    DP: 0.9404234367306845,
                    "DP norm": 0.9404234367306845,
                    "KL-divergence": 4.327988486204692,
                    DA: 0.015055921995985266,
                    X: 22.0,
                    Xpos: 0.33574935353791374,
                    Y: 0.0547538064485841,
                    Ypos: 0.18027382490427576,
                    Expected: 0.05228688039529833,
                    Residual: 0.002466926053285773,
                    ColorScore: 0.5072124241518663,
                },
                s: NaN,
                os: 0,
                bg: 0.021432050657574284,
            }, {
                x: 0.27691330811132914,
                y: 0.16021978669868825,
                ox: 18,
                oy: 0.04909299996451014,
                term: "kripto",
                cat25k: 222,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 18,
                ncat: 0,
                etc: {
                    Frequency: 18.0,
                    Range: 17.0,
                    SD: 0.12473669936901104,
                    VC: 8.793937305515279,
                    "Juilland's D": 0.72516516318915,
                    "Rosengren's S": 0.04909299996451014,
                    DP: 0.9473165928114355,
                    "DP norm": 0.9473165928114355,
                    "KL-divergence": 4.457683495829369,
                    DA: 0.01191728005608128,
                    X: 18.0,
                    Xpos: 0.27691330811132914,
                    Y: 0.04909299996451014,
                    Ypos: 0.16021978669868825,
                    Expected: 0.04923525213023862,
                    Residual: -0.00014225216572848198,
                    ColorScore: 0.499584104698076,
                },
                s: NaN,
                os: 0,
                bg: 0.017569546120058566,
            }, {
                x: 0.32210982462295945,
                y: 0.23331778736472608,
                ox: 21,
                oy: 0.06972693074199603,
                term: "olarak",
                cat25k: 258,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 21,
                ncat: 0,
                etc: {
                    Frequency: 21.0,
                    Range: 20.0,
                    SD: 0.1336063465810382,
                    VC: 8.073640657682738,
                    "Juilland's D": 0.7592182235307368,
                    "Rosengren's S": 0.06972693074199603,
                    DP: 0.9271294928606706,
                    "DP norm": 0.9271294928606706,
                    "KL-divergence": 3.9085594016665373,
                    DA: 0.014270692504131044,
                    X: 21.0,
                    Xpos: 0.32210982462295945,
                    Y: 0.06972693074199603,
                    Ypos: 0.23331778736472608,
                    Expected: 0.05028199765878749,
                    Residual: 0.019444933083208535,
                    ColorScore: 0.5568501454731326,
                },
                s: NaN,
                os: 0,
                bg: 0.0006757409016314316,
            }, {
                x: 0.6666119773274264,
                y: 0.49735190376273064,
                ox: 68,
                oy: 0.14425785677294986,
                term: "yorum",
                cat25k: 837,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 68,
                ncat: 0,
                etc: {
                    Frequency: 68.0,
                    Range: 62.0,
                    SD: 0.2547518237513817,
                    VC: 4.754118593242697,
                    "Juilland's D": 0.8464085623860196,
                    "Rosengren's S": 0.14425785677294986,
                    DP: 0.8404726735598301,
                    "DP norm": 0.8404726735598301,
                    "KL-divergence": 2.9404593338252676,
                    DA: 0.044001670068658405,
                    X: 68.0,
                    Xpos: 0.6666119773274264,
                    Y: 0.14425785677294986,
                    Ypos: 0.49735190376273064,
                    Expected: 0.09614092908958558,
                    Residual: 0.048116927683364286,
                    ColorScore: 0.6406769736266995,
                },
                s: NaN,
                os: 0,
                bg: 0.0647927584564078,
            }, {
                x: 0.6874148132928187,
                y: 0.49984888220768914,
                ox: 73,
                oy: 0.14496269794393535,
                term: "daha",
                cat25k: 899,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 73,
                ncat: 0,
                etc: {
                    Frequency: 73.0,
                    Range: 64.0,
                    SD: 0.2704236387218252,
                    VC: 4.70092599367118,
                    "Juilland's D": 0.8517186276628048,
                    "Rosengren's S": 0.14496269794393535,
                    DP: 0.8380108321024212,
                    "DP norm": 0.8380108321024212,
                    "KL-divergence": 2.9352735104843917,
                    DA: 0.04394797113348614,
                    X: 73.0,
                    Xpos: 0.6874148132928187,
                    Y: 0.14496269794393535,
                    Ypos: 0.49984888220768914,
                    Expected: 0.11512497028282875,
                    Residual: 0.029837727661106594,
                    ColorScore: 0.5872350216307213,
                },
                s: NaN,
                os: 0,
                bg: 0.0021713588839810225,
            }, {
                x: 0.27691330811132914,
                y: 0.1445010200206257,
                ox: 18,
                oy: 0.04465594367586548,
                term: "fazla",
                cat25k: 222,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 18,
                ncat: 0,
                etc: {
                    Frequency: 18.0,
                    Range: 18.0,
                    SD: 0.11825058156406429,
                    VC: 8.336666000266533,
                    "Juilland's D": 0.7119418692628885,
                    "Rosengren's S": 0.04465594367586548,
                    DP: 0.9473165928114327,
                    "DP norm": 0.9473165928114327,
                    "KL-divergence": 4.714003552202794,
                    DA: 0.01340694006309151,
                    X: 18.0,
                    Xpos: 0.27691330811132914,
                    Y: 0.04465594367586548,
                    Ypos: 0.1445010200206257,
                    Expected: 0.04923525213023862,
                    Residual: -0.0045793084543731405,
                    ColorScore: 0.48661171264084896,
                },
                s: NaN,
                os: 0,
                bg: 0.0017457084666860636,
            }, {
                x: 0.1325206812656045,
                y: 0.06530420654322973,
                ox: 11,
                oy: 0.022300454439491715,
                term: "olabilir",
                cat25k: 135,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 11,
                ncat: 0,
                etc: {
                    Frequency: 11.0,
                    Range: 11.0,
                    SD: 0.09269899826374953,
                    VC: 10.694093526972559,
                    "Juilland's D": 0.6085956410876506,
                    "Rosengren's S": 0.022300454439491715,
                    DP: 0.9734121122599844,
                    "DP norm": 0.9734121122599844,
                    "KL-divergence": 5.776134910941839,
                    DA: 0.007886435331230235,
                    X: 11.0,
                    Xpos: 0.1325206812656045,
                    Y: 0.022300454439491715,
                    Ypos: 0.06530420654322973,
                    Expected: 0.021504079936589475,
                    Residual: 0.0007963745029022397,
                    ColorScore: 0.5023283189583296,
                },
                s: NaN,
                os: 0,
                bg: 0.010773751224289911,
            }, {
                x: 0.10457602270114133,
                y: 0.0874231951078478,
                ox: 10,
                oy: 0.02854415022804672,
                term: "projeye",
                cat25k: 123,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 10,
                ncat: 0,
                etc: {
                    Frequency: 10.0,
                    Range: 10.0,
                    SD: 0.08842014911062773,
                    VC: 11.22051692213866,
                    "Juilland's D": 0.6588056130077559,
                    "Rosengren's S": 0.02854415022804672,
                    DP: 0.9704579025110893,
                    "DP norm": 0.9704579025110893,
                    "KL-divergence": 5.183965583597691,
                    DA: 0.007097791798107211,
                    X: 10.0,
                    Xpos: 0.10457602270114133,
                    Y: 0.02854415022804672,
                    Ypos: 0.0874231951078478,
                    Expected: 0.025393729342041836,
                    Residual: 0.003150420886004885,
                    ColorScore: 0.5092107226548203,
                },
                s: NaN,
                os: 0,
                bg: 0.009799118079372858,
            }, {
                x: 0.0391510034100286,
                y: 0.11230372178019,
                ox: 8,
                oy: 0.035567366463604096,
                term: "almak",
                cat25k: 98,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 8,
                ncat: 0,
                etc: {
                    Frequency: 8.0,
                    Range: 8.0,
                    SD: 0.07914817670285086,
                    VC: 12.554879529489718,
                    "Juilland's D": 0.5853818871285621,
                    "Rosengren's S": 0.035567366463604096,
                    DP: 0.9615952732644109,
                    "DP norm": 0.9615952732644109,
                    "KL-divergence": 4.933609861234693,
                    DA: 0.0055205047318613865,
                    X: 8.0,
                    Xpos: 0.0391510034100286,
                    Y: 0.035567366463604096,
                    Ypos: 0.11230372178019,
                    Expected: 0.020969598587433753,
                    Residual: 0.014597767876170342,
                    ColorScore: 0.5426787391754999,
                },
                s: NaN,
                os: 0,
                bg: 0.000995891945723889,
            }, {
                x: 0.47188236383573096,
                y: 0.2389905437352424,
                ox: 35,
                oy: 0.07132822299623355,
                term: "istiyorum",
                cat25k: 431,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 35,
                ncat: 0,
                etc: {
                    Frequency: 35.0,
                    Range: 35.0,
                    SD: 0.16376835244660606,
                    VC: 5.9377725501355165,
                    "Juilland's D": 0.7935151515407476,
                    "Rosengren's S": 0.07132822299623355,
                    DP: 0.9217134416543671,
                    "DP norm": 0.9217134416543671,
                    "KL-divergence": 3.9519556952501698,
                    DA: 0.02681388012618313,
                    X: 35.0,
                    Xpos: 0.47188236383573096,
                    Y: 0.07132822299623355,
                    Ypos: 0.2389905437352424,
                    Expected: 0.07146581635466058,
                    Residual: -0.00013759335842702947,
                    ColorScore: 0.49959772541210395,
                },
                s: NaN,
                os: 0,
                bg: 0.03388189738625363,
            }, {
                x: 0.37322971426456303,
                y: 0.26815878876924226,
                ox: 25,
                oy: 0.07956176623200538,
                term: "katk",
                cat25k: 308,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 25,
                ncat: 0,
                etc: {
                    Frequency: 25.0,
                    Range: 25.0,
                    SD: 0.13896920479549563,
                    VC: 7.054076835419358,
                    "Juilland's D": 0.7340516597977242,
                    "Rosengren's S": 0.07956176623200538,
                    DP: 0.9158050221565831,
                    "DP norm": 0.9158050221565831,
                    "KL-divergence": 3.7530493263377536,
                    DA: 0.018927444794952786,
                    X: 25.0,
                    Xpos: 0.37322971426456303,
                    Y: 0.07956176623200538,
                    Ypos: 0.26815878876924226,
                    Expected: 0.06393679744898163,
                    Residual: 0.015624968783023746,
                    ColorScore: 0.5456819133563963,
                },
                s: NaN,
                os: 0,
                bg: 0.024319066147859923,
            }, {
                x: 0.32210982462295945,
                y: 0.29030985842963913,
                ox: 21,
                oy: 0.08581451779641655,
                term: "ile",
                cat25k: 258,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 21,
                ncat: 0,
                etc: {
                    Frequency: 21.0,
                    Range: 21.0,
                    SD: 0.12757198641354173,
                    VC: 7.70899289327545,
                    "Juilland's D": 0.7545097183763108,
                    "Rosengren's S": 0.08581451779641655,
                    DP: 0.9098966026588007,
                    "DP norm": 0.9098966026588007,
                    "KL-divergence": 3.6220805577720725,
                    DA: 0.01577287066246047,
                    X: 21.0,
                    Xpos: 0.32210982462295945,
                    Y: 0.08581451779641655,
                    Ypos: 0.29030985842963913,
                    Expected: 0.05028199765878749,
                    Residual: 0.03553252013762906,
                    ColorScore: 0.6038845919503627,
                },
                s: NaN,
                os: 0,
                bg: 9.267570651986834e-6,
            }, {
                x: 0.36126082803298815,
                y: 0.23411241260463686,
                ox: 24,
                oy: 0.06995123567571469,
                term: "ula",
                cat25k: 295,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 24,
                ncat: 0,
                etc: {
                    Frequency: 24.0,
                    Range: 24.0,
                    SD: 0.1362161729634793,
                    VC: 7.202430145443968,
                    "Juilland's D": 0.7371874882622316,
                    "Rosengren's S": 0.06995123567571469,
                    DP: 0.9226981782373325,
                    "DP norm": 0.9226981782373325,
                    "KL-divergence": 3.9909727139112032,
                    DA: 0.01813880126182965,
                    X: 24.0,
                    Xpos: 0.36126082803298815,
                    Y: 0.06995123567571469,
                    Ypos: 0.23411241260463686,
                    Expected: 0.06230915514437131,
                    Residual: 0.0076420805313433815,
                    ColorScore: 0.5223427557227972,
                },
                s: NaN,
                os: 0,
                bg: 0.0002695432925836286,
            }, {
                x: 0.0,
                y: 0.07707602070054305,
                ox: 7,
                oy: 0.025623374303704708,
                term: "abilirsiniz",
                cat25k: 86,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 7,
                ncat: 0,
                etc: {
                    Frequency: 7.0,
                    Range: 7.0,
                    SD: 0.07406569038618868,
                    VC: 13.427051585724776,
                    "Juilland's D": 0.6027872212443297,
                    "Rosengren's S": 0.025623374303704708,
                    DP: 0.9734121122599843,
                    "DP norm": 0.9734121122599843,
                    "KL-divergence": 5.3374164274293125,
                    DA: 0.004731861198738252,
                    X: 7.0,
                    Xpos: 0.0,
                    Y: 0.025623374303704708,
                    Ypos: 0.07707602070054305,
                    Expected: 0.022260856221882664,
                    Residual: 0.003362518081822044,
                    ColorScore: 0.509830820259942,
                },
                s: NaN,
                os: 0,
                bg: 0.006869479882237487,
            }, {
                x: 0.27691330811132914,
                y: 0.20284504991165922,
                ox: 18,
                oy: 0.06112515847082613,
                term: "projenin",
                cat25k: 222,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 18,
                ncat: 0,
                etc: {
                    Frequency: 18.0,
                    Range: 16.0,
                    SD: 0.13090182694947639,
                    VC: 9.228578799938086,
                    "Juilland's D": 0.7107593130375705,
                    "Rosengren's S": 0.06112515847082613,
                    DP: 0.9364844903988292,
                    "DP norm": 0.9364844903988292,
                    "KL-divergence": 4.095628078527607,
                    DA: 0.01060287416754302,
                    X: 18.0,
                    Xpos: 0.27691330811132914,
                    Y: 0.06112515847082613,
                    Ypos: 0.20284504991165922,
                    Expected: 0.04923525213023862,
                    Residual: 0.011889906340587508,
                    ColorScore: 0.5347619044113875,
                },
                s: NaN,
                os: 0,
                bg: 0.017569546120058566,
            }, {
                x: 0.27691330811132914,
                y: 0.12635999513307578,
                ox: 18,
                oy: 0.039535138067617596,
                term: "bende",
                cat25k: 222,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 18,
                ncat: 0,
                etc: {
                    Frequency: 18.0,
                    Range: 18.0,
                    SD: 0.11825058156406429,
                    VC: 8.336666000266533,
                    "Juilland's D": 0.7010345711268113,
                    "Rosengren's S": 0.039535138067617596,
                    DP: 0.9551944854751444,
                    "DP norm": 0.9551944854751444,
                    "KL-divergence": 4.847498815862291,
                    DA: 0.01340694006309151,
                    X: 18.0,
                    Xpos: 0.27691330811132914,
                    Y: 0.039535138067617596,
                    Ypos: 0.12635999513307578,
                    Expected: 0.04923525213023862,
                    Residual: -0.009700114062621022,
                    ColorScore: 0.4716402780505228,
                },
                s: NaN,
                os: 0,
                bg: 0.0010651833002929254,
            }, {
                x: 0.0,
                y: 0.07775066444296304,
                ox: 7,
                oy: 0.025813811144024822,
                term: "destek",
                cat25k: 86,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 7,
                ncat: 0,
                etc: {
                    Frequency: 7.0,
                    Range: 6.0,
                    SD: 0.08403434191816095,
                    VC: 15.23422569916375,
                    "Juilland's D": 0.3494023896015631,
                    "Rosengren's S": 0.025813811144024822,
                    DP: 0.9719350073855377,
                    "DP norm": 0.9719350073855377,
                    "KL-divergence": 5.468089870350428,
                    DA: 0.0033799008562415134,
                    X: 7.0,
                    Xpos: 0.0,
                    Y: 0.025813811144024822,
                    Ypos: 0.07775066444296304,
                    Expected: 0.022260856221882664,
                    Residual: 0.0035529549221421583,
                    ColorScore: 0.5103875906036255,
                },
                s: NaN,
                os: 0,
                bg: 0.006869479882237487,
            }, {
                x: 0.32210982462295945,
                y: 0.033463583491372614,
                ox: 21,
                oy: 0.013312558656053554,
                term: "evet",
                cat25k: 258,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 21,
                ncat: 0,
                etc: {
                    Frequency: 21.0,
                    Range: 21.0,
                    SD: 0.12757198641354173,
                    VC: 7.70899289327545,
                    "Juilland's D": 0.7747236963595292,
                    "Rosengren's S": 0.013312558656053554,
                    DP: 0.985721319547031,
                    "DP norm": 0.985721319547031,
                    "KL-divergence": 6.309942815803108,
                    DA: 0.01577287066246047,
                    X: 21.0,
                    Xpos: 0.32210982462295945,
                    Y: 0.013312558656053554,
                    Ypos: 0.033463583491372614,
                    Expected: 0.05028199765878749,
                    Residual: -0.03696943900273394,
                    ColorScore: 0.3919143626582884,
                },
                s: NaN,
                os: 0,
                bg: 0.02046783625730994,
            }, {
                x: 0.37322971426456303,
                y: 0.16431581926265787,
                ox: 25,
                oy: 0.05024921835102129,
                term: "lar",
                cat25k: 308,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 25,
                ncat: 0,
                etc: {
                    Frequency: 25.0,
                    Range: 23.0,
                    SD: 0.14988171382781704,
                    VC: 7.607995793899993,
                    "Juilland's D": 0.7376534358540354,
                    "Rosengren's S": 0.05024921835102129,
                    DP: 0.9384539635647571,
                    "DP norm": 0.9384539635647571,
                    "KL-divergence": 4.653684805412226,
                    DA: 0.01602523659305999,
                    X: 25.0,
                    Xpos: 0.37322971426456303,
                    Y: 0.05024921835102129,
                    Ypos: 0.16431581926265787,
                    Expected: 0.06393679744898163,
                    Residual: -0.013687579097960346,
                    ColorScore: 0.4599823326948854,
                },
                s: NaN,
                os: 0,
                bg: 4.6466371822048674e-5,
            }, {
                x: 0.2927656550592527,
                y: 0.15644692180767764,
                ox: 19,
                oy: 0.04802800458454635,
                term: "yat",
                cat25k: 234,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 19,
                ncat: 0,
                etc: {
                    Frequency: 19.0,
                    Range: 17.0,
                    SD: 0.1337921303690111,
                    VC: 8.935905970435531,
                    "Juilland's D": 0.7263209077314668,
                    "Rosengren's S": 0.04802800458454635,
                    DP: 0.9468242245199501,
                    "DP norm": 0.9468242245199501,
                    "KL-divergence": 4.520665142265546,
                    DA: 0.011373069898721666,
                    X: 19.0,
                    Xpos: 0.2927656550592527,
                    Y: 0.04802800458454635,
                    Ypos: 0.15644692180767764,
                    Expected: 0.050026137081742104,
                    Residual: -0.0019981324971957565,
                    ColorScore: 0.4941581633295377,
                },
                s: NaN,
                os: 0,
                bg: 0.00012246252807775727,
            }, {
                x: 0.0,
                y: 0.04758931706578312,
                ox: 7,
                oy: 0.017299937327150572,
                term: "uzun",
                cat25k: 86,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 7,
                ncat: 0,
                etc: {
                    Frequency: 7.0,
                    Range: 7.0,
                    SD: 0.07406569038618868,
                    VC: 13.427051585724776,
                    "Juilland's D": 0.5733672770346736,
                    "Rosengren's S": 0.017299937327150572,
                    DP: 0.9817823732151788,
                    "DP norm": 0.9817823732151788,
                    "KL-divergence": 5.9348093469777545,
                    DA: 0.004731861198738252,
                    X: 7.0,
                    Xpos: 0.0,
                    Y: 0.017299937327150572,
                    Ypos: 0.04758931706578312,
                    Expected: 0.022260856221882664,
                    Residual: -0.004960918894732092,
                    ColorScore: 0.4854960179271856,
                },
                s: NaN,
                os: 0,
                bg: 0.0007481430021909901,
            }, {
                x: 0.07368463583902007,
                y: 0.03096735828906276,
                ox: 9,
                oy: 0.01260793010862178,
                term: "her",
                cat25k: 111,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 9,
                ncat: 0,
                etc: {
                    Frequency: 9.0,
                    Range: 9.0,
                    SD: 0.08391602529219312,
                    VC: 11.83215956619923,
                    "Juilland's D": 0.6506473513357034,
                    "Rosengren's S": 0.01260793010862178,
                    DP: 0.9867060561299976,
                    "DP norm": 0.9867060561299976,
                    "KL-divergence": 6.3761295313538495,
                    DA: 0.006309148264984299,
                    X: 9.0,
                    Xpos: 0.07368463583902007,
                    Y: 0.01260793010862178,
                    Ypos: 0.03096735828906276,
                    Expected: 0.026809092001212464,
                    Residual: -0.014201161892590684,
                    ColorScore: 0.4584807972325471,
                },
                s: NaN,
                os: 0,
                bg: 4.592269005443959e-8,
            }, {
                x: 0.0391510034100286,
                y: 0.058773807669354625,
                ox: 8,
                oy: 0.020457068887422627,
                term: "zaman",
                cat25k: 98,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 8,
                ncat: 0,
                etc: {
                    Frequency: 8.0,
                    Range: 7.0,
                    SD: 0.08854647369952867,
                    VC: 14.045684390587734,
                    "Juilland's D": 0.5767351248046533,
                    "Rosengren's S": 0.020457068887422627,
                    DP: 0.9778434268833182,
                    "DP norm": 0.9778434268833182,
                    "KL-divergence": 5.713649152401406,
                    DA: 0.004140378548895929,
                    X: 8.0,
                    Xpos: 0.0391510034100286,
                    Y: 0.020457068887422627,
                    Ypos: 0.058773807669354625,
                    Expected: 0.020969598587433753,
                    Residual: -0.0005125297000111266,
                    ColorScore: 0.4985015434159506,
                },
                s: NaN,
                os: 0,
                bg: 6.617969441526103e-5,
            }, {
                x: 0.39579446046197947,
                y: 0.18695562069407592,
                ox: 27,
                oy: 0.056639927964081176,
                term: "yeni",
                cat25k: 332,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 27,
                ncat: 0,
                etc: {
                    Frequency: 27.0,
                    Range: 26.0,
                    SD: 0.14966611623020726,
                    VC: 7.034307462819742,
                    "Juilland's D": 0.7382154669874951,
                    "Rosengren's S": 0.056639927964081176,
                    DP: 0.9364844903988278,
                    "DP norm": 0.9364844903988278,
                    "KL-divergence": 4.344906802822607,
                    DA: 0.018985862834443368,
                    X: 27.0,
                    Xpos: 0.39579446046197947,
                    Y: 0.056639927964081176,
                    Ypos: 0.18695562069407592,
                    Expected: 0.06349492861282878,
                    Residual: -0.006855000648747604,
                    ColorScore: 0.47995838903471216,
                },
                s: NaN,
                os: 0,
                bg: 0.0004280109380573059,
            }, {
                x: 0.1325206812656045,
                y: 0.049596761293332806,
                ox: 11,
                oy: 0.01786659393681854,
                term: "sonra",
                cat25k: 135,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 11,
                ncat: 0,
                etc: {
                    Frequency: 11.0,
                    Range: 11.0,
                    SD: 0.09269899826374953,
                    VC: 10.694093526972559,
                    "Juilland's D": 0.6469744690713275,
                    "Rosengren's S": 0.01786659393681854,
                    DP: 0.9807976366322136,
                    "DP norm": 0.9807976366322136,
                    "KL-divergence": 5.921267469083565,
                    DA: 0.007886435331230235,
                    X: 11.0,
                    Xpos: 0.1325206812656045,
                    Y: 0.01786659393681854,
                    Ypos: 0.049596761293332806,
                    Expected: 0.021504079936589475,
                    Residual: -0.0036374859997709355,
                    ColorScore: 0.48936527025531223,
                },
                s: NaN,
                os: 0,
                bg: 0.000852680128677183,
            }, {
                x: 0.15803215576067894,
                y: 0.11058993931171916,
                ox: 12,
                oy: 0.03508360400088429,
                term: "yap",
                cat25k: 148,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 12,
                ncat: 0,
                etc: {
                    Frequency: 12.0,
                    Range: 10.0,
                    SD: 0.11188803372292416,
                    VC: 11.83215956619923,
                    "Juilland's D": 0.6605543021336628,
                    "Rosengren's S": 0.03508360400088429,
                    DP: 0.9625800098473742,
                    "DP norm": 0.9625800098473742,
                    "KL-divergence": 4.920006873927053,
                    DA: 0.006046267087276513,
                    X: 12.0,
                    Xpos: 0.15803215576067894,
                    Y: 0.03508360400088429,
                    Ypos: 0.11058993931171916,
                    Expected: 0.02879902189510588,
                    Residual: 0.006284582105778411,
                    ColorScore: 0.5183739077641709,
                },
                s: NaN,
                os: 0,
                bg: 3.594412485790838e-5,
            }, {
                x: 0.6299145195964098,
                y: 0.2625445148558661,
                ox: 60,
                oy: 0.07797698226747936,
                term: "zel",
                cat25k: 739,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 60,
                ncat: 0,
                etc: {
                    Frequency: 60.0,
                    Range: 59.0,
                    SD: 0.2159209216790628,
                    VC: 4.566727493512178,
                    "Juilland's D": 0.8506425566073798,
                    "Rosengren's S": 0.07797698226747936,
                    DP: 0.9084194977843519,
                    "DP norm": 0.9084194977843519,
                    "KL-divergence": 3.899718407928372,
                    DA: 0.044978969505783395,
                    X: 60.0,
                    Xpos: 0.6299145195964098,
                    Y: 0.07797698226747936,
                    Ypos: 0.2625445148558661,
                    Expected: 0.09614092908958558,
                    Residual: -0.018163946822106217,
                    ColorScore: 0.44689500782624475,
                },
                s: NaN,
                os: 0,
                bg: 0.0014717605936101063,
            }, {
                x: 0.2601546327828081,
                y: 0.13948411888806023,
                ox: 17,
                oy: 0.04323978468733459,
                term: "reklam",
                cat25k: 209,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 17,
                ncat: 0,
                etc: {
                    Frequency: 17.0,
                    Range: 16.0,
                    SD: 0.12162629798673717,
                    VC: 9.079045420304086,
                    "Juilland's D": 0.6855726251741581,
                    "Rosengren's S": 0.04323978468733459,
                    DP: 0.9497784342688422,
                    "DP norm": 0.9497784342688422,
                    "KL-divergence": 4.7513965164009635,
                    DA: 0.011133791055854547,
                    X: 17.0,
                    Xpos: 0.2601546327828081,
                    Y: 0.04323978468733459,
                    Ypos: 0.13948411888806023,
                    Expected: 0.044595237512910474,
                    Residual: -0.0013554528255758855,
                    ColorScore: 0.49603713265629595,
                },
                s: NaN,
                os: 0,
                bg: 0.0009666505558240697,
            }, {
                x: 0.39579446046197947,
                y: 0.3624108611164656,
                ox: 27,
                oy: 0.10616701834187287,
                term: "nda",
                cat25k: 332,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 27,
                ncat: 0,
                etc: {
                    Frequency: 27.0,
                    Range: 27.0,
                    SD: 0.14430489325798446,
                    VC: 6.78232998312527,
                    "Juilland's D": 0.7029959479191007,
                    "Rosengren's S": 0.10616701834187287,
                    DP: 0.8838010832102505,
                    "DP norm": 0.8838010832102505,
                    "KL-divergence": 3.4257698901715203,
                    DA: 0.02050473186119872,
                    X: 27.0,
                    Xpos: 0.39579446046197947,
                    Y: 0.10616701834187287,
                    Ypos: 0.3624108611164656,
                    Expected: 0.06349492861282878,
                    Residual: 0.042672089729044085,
                    ColorScore: 0.6247581824199538,
                },
                s: NaN,
                os: 0,
                bg: 7.258347435585526e-5,
            }, {
                x: 0.07368463583902007,
                y: 0.08248380692379799,
                ox: 9,
                oy: 0.027149871411332543,
                term: "biraz",
                cat25k: 111,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 9,
                ncat: 0,
                etc: {
                    Frequency: 9.0,
                    Range: 9.0,
                    SD: 0.08391602529219312,
                    VC: 11.83215956619923,
                    "Juilland's D": 0.6109358161552167,
                    "Rosengren's S": 0.027149871411332543,
                    DP: 0.9704579025110913,
                    "DP norm": 0.9704579025110913,
                    "KL-divergence": 5.3333586544190545,
                    DA: 0.006309148264984299,
                    X: 9.0,
                    Xpos: 0.07368463583902007,
                    Y: 0.027149871411332543,
                    Ypos: 0.08248380692379799,
                    Expected: 0.026809092001212464,
                    Residual: 0.00034077941012007965,
                    ColorScore: 0.5009963191416845,
                },
                s: NaN,
                os: 0,
                bg: 0.008823529411764706,
            }, {
                x: 0.32210982462295945,
                y: 0.14657046730300008,
                ox: 21,
                oy: 0.0452401023612344,
                term: "kazan",
                cat25k: 258,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 21,
                ncat: 0,
                etc: {
                    Frequency: 21.0,
                    Range: 21.0,
                    SD: 0.12757198641354173,
                    VC: 7.70899289327545,
                    "Juilland's D": 0.7155553523914914,
                    "Rosengren's S": 0.0452401023612344,
                    DP: 0.949778434268841,
                    "DP norm": 0.949778434268841,
                    "KL-divergence": 4.642329491745353,
                    DA: 0.01577287066246047,
                    X: 21.0,
                    Xpos: 0.32210982462295945,
                    Y: 0.0452401023612344,
                    Ypos: 0.14657046730300008,
                    Expected: 0.05028199765878749,
                    Residual: -0.005041895297553091,
                    ColorScore: 0.48525927140506775,
                },
                s: NaN,
                os: 0,
                bg: 8.815306730696578e-5,
            }, {
                x: 0.36126082803298815,
                y: 0.15094768192474775,
                ox: 24,
                oy: 0.046475692154120535,
                term: "uygulama",
                cat25k: 295,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 24,
                ncat: 0,
                etc: {
                    Frequency: 24.0,
                    Range: 24.0,
                    SD: 0.1362161729634793,
                    VC: 7.202430145443968,
                    "Juilland's D": 0.7546122793185874,
                    "Rosengren's S": 0.046475692154120535,
                    DP: 0.947808961102917,
                    "DP norm": 0.947808961102917,
                    "KL-divergence": 4.598050030924991,
                    DA: 0.01813880126182965,
                    X: 24.0,
                    Xpos: 0.36126082803298815,
                    Y: 0.046475692154120535,
                    Ypos: 0.15094768192474775,
                    Expected: 0.06230915514437131,
                    Residual: -0.015833462990250777,
                    ColorScore: 0.4537085229099338,
                },
                s: NaN,
                os: 0,
                bg: 0.023357664233576644,
            }, {
                x: 0.0,
                y: 0.10444922676811128,
                ox: 7,
                oy: 0.03335021818465479,
                term: "malar",
                cat25k: 86,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 7,
                ncat: 0,
                etc: {
                    Frequency: 7.0,
                    Range: 7.0,
                    SD: 0.07406569038618868,
                    VC: 13.427051585724776,
                    "Juilland's D": 0.5461227468392384,
                    "Rosengren's S": 0.03335021818465479,
                    DP: 0.9645494830133061,
                    "DP norm": 0.9645494830133061,
                    "KL-divergence": 5.008835693603776,
                    DA: 0.004731861198738252,
                    X: 7.0,
                    Xpos: 0.0,
                    Y: 0.03335021818465479,
                    Ypos: 0.10444922676811128,
                    Expected: 0.022260856221882664,
                    Residual: 0.011089361962772128,
                    ColorScore: 0.5324213942053738,
                },
                s: NaN,
                os: 0,
                bg: 0.0002693965517241379,
            }, {
                x: 0.22345717505179155,
                y: 0.06894009547193376,
                ox: 15,
                oy: 0.023326784568714565,
                term: "ekk",
                cat25k: 185,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 15,
                ncat: 0,
                etc: {
                    Frequency: 15.0,
                    Range: 15.0,
                    SD: 0.1080768742379429,
                    VC: 9.14330356052997,
                    "Juilland's D": 0.6966229294642081,
                    "Rosengren's S": 0.023326784568714565,
                    DP: 0.9709502708025731,
                    "DP norm": 0.9709502708025731,
                    "KL-divergence": 5.72479753482658,
                    DA: 0.011041009463722329,
                    X: 15.0,
                    Xpos: 0.22345717505179155,
                    Y: 0.023326784568714565,
                    Ypos: 0.06894009547193376,
                    Expected: 0.036184508831817654,
                    Residual: -0.012857724263103089,
                    ColorScore: 0.4624085363686824,
                },
                s: NaN,
                os: 0,
                bg: 0.014662756598240467,
            }, {
                x: 0.0,
                y: 0.03927420215613754,
                ox: 7,
                oy: 0.014952766352716754,
                term: "ederim",
                cat25k: 86,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 7,
                ncat: 0,
                etc: {
                    Frequency: 7.0,
                    Range: 7.0,
                    SD: 0.07406569038618868,
                    VC: 13.427051585724776,
                    "Juilland's D": 0.5163075734418549,
                    "Rosengren's S": 0.014952766352716754,
                    DP: 0.9827671097981452,
                    "DP norm": 0.9827671097981452,
                    "KL-divergence": 6.282704999543942,
                    DA: 0.004731861198738252,
                    X: 7.0,
                    Xpos: 0.0,
                    Y: 0.014952766352716754,
                    Ypos: 0.03927420215613754,
                    Expected: 0.022260856221882664,
                    Residual: -0.00730808986916591,
                    ColorScore: 0.4786337155075334,
                },
                s: NaN,
                os: 0,
                bg: 0.006869479882237487,
            }, {
                x: 0.20322867227230915,
                y: 0.08516838874495573,
                ox: 14,
                oy: 0.02790766881973693,
                term: "hem",
                cat25k: 172,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 14,
                ncat: 0,
                etc: {
                    Frequency: 14.0,
                    Range: 8.0,
                    SD: 0.1427125146590005,
                    VC: 12.935870078733688,
                    "Juilland's D": 0.5817809126242937,
                    "Rosengren's S": 0.02790766881973693,
                    DP: 0.9689807976366462,
                    "DP norm": 0.9689807976366462,
                    "KL-divergence": 5.307794448663605,
                    DA: 0.004844524560613017,
                    X: 14.0,
                    Xpos: 0.20322867227230915,
                    Y: 0.02790766881973693,
                    Ypos: 0.08516838874495573,
                    Expected: 0.03618450883181766,
                    Residual: -0.00827684001208073,
                    ColorScore: 0.4758014308030217,
                },
                s: NaN,
                os: 0,
                bg: 1.3548345577650651e-5,
            }, {
                x: 0.0391510034100286,
                y: 0.030055396489632107,
                ox: 8,
                oy: 0.01235050368834068,
                term: "uygulamay",
                cat25k: 98,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 8,
                ncat: 0,
                etc: {
                    Frequency: 8.0,
                    Range: 7.0,
                    SD: 0.08854647369952867,
                    VC: 14.045684390587734,
                    "Juilland's D": 0.6000019712225753,
                    "Rosengren's S": 0.01235050368834068,
                    DP: 0.9871984244214783,
                    "DP norm": 0.9871984244214783,
                    "KL-divergence": 6.389895168601463,
                    DA: 0.004140378548895929,
                    X: 8.0,
                    Xpos: 0.0391510034100286,
                    Y: 0.01235050368834068,
                    Ypos: 0.030055396489632107,
                    Expected: 0.020969598587433753,
                    Residual: -0.008619094899093073,
                    ColorScore: 0.47480079788583546,
                },
                s: NaN,
                os: 0,
                bg: 0.00784698381559588,
            }, {
                x: 0.0,
                y: 0.06472832839729081,
                ox: 7,
                oy: 0.022137896918201106,
                term: "uygulamaya",
                cat25k: 86,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 7,
                ncat: 0,
                etc: {
                    Frequency: 7.0,
                    Range: 7.0,
                    SD: 0.07406569038618868,
                    VC: 13.427051585724776,
                    "Juilland's D": 0.6066272996570088,
                    "Rosengren's S": 0.022137896918201106,
                    DP: 0.9773510585918372,
                    "DP norm": 0.9773510585918372,
                    "KL-divergence": 5.53051291861237,
                    DA: 0.004731861198738252,
                    X: 7.0,
                    Xpos: 0.0,
                    Y: 0.022137896918201106,
                    Ypos: 0.06472832839729081,
                    Expected: 0.022260856221882664,
                    Residual: -0.00012295930368155794,
                    ColorScore: 0.49964051024132305,
                },
                s: NaN,
                os: 0,
                bg: 0.006869479882237487,
            }, {
                x: 0.15803215576067894,
                y: 0.06224666852280534,
                ox: 12,
                oy: 0.021437379837065826,
                term: "uan",
                cat25k: 148,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 12,
                ncat: 0,
                etc: {
                    Frequency: 12.0,
                    Range: 12.0,
                    SD: 0.09678245621966297,
                    VC: 10.23474474522936,
                    "Juilland's D": 0.6877033717017806,
                    "Rosengren's S": 0.021437379837065826,
                    DP: 0.9758739537173917,
                    "DP norm": 0.9758739537173917,
                    "KL-divergence": 5.681197182093998,
                    DA: 0.00867507886435337,
                    X: 12.0,
                    Xpos: 0.15803215576067894,
                    Y: 0.021437379837065826,
                    Ypos: 0.06224666852280534,
                    Expected: 0.02879902189510588,
                    Residual: -0.0073616420580400535,
                    ColorScore: 0.4784771477417884,
                },
                s: NaN,
                os: 0,
                bg: 0.00029691946059631324,
            }, {
                x: 0.07368463583902007,
                y: 0.12982075346034383,
                ox: 9,
                oy: 0.040512032744788075,
                term: "projesi",
                cat25k: 111,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 9,
                ncat: 0,
                etc: {
                    Frequency: 9.0,
                    Range: 9.0,
                    SD: 0.08391602529219312,
                    VC: 11.83215956619923,
                    "Juilland's D": 0.635300934587241,
                    "Rosengren's S": 0.040512032744788075,
                    DP: 0.9576563269325546,
                    "DP norm": 0.9576563269325546,
                    "KL-divergence": 4.693365942760254,
                    DA: 0.006309148264984299,
                    X: 9.0,
                    Xpos: 0.07368463583902007,
                    Y: 0.040512032744788075,
                    Ypos: 0.12982075346034383,
                    Expected: 0.026809092001212464,
                    Residual: 0.013702940743575611,
                    ColorScore: 0.5400625793541403,
                },
                s: NaN,
                os: 0,
                bg: 0.008823529411764706,
            }, {
                x: 0.15803215576067894,
                y: 0.10360933903068172,
                ox: 12,
                oy: 0.03311313666016608,
                term: "var",
                cat25k: 148,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 12,
                ncat: 0,
                etc: {
                    Frequency: 12.0,
                    Range: 12.0,
                    SD: 0.09678245621966297,
                    VC: 10.23474474522936,
                    "Juilland's D": 0.6229614548585242,
                    "Rosengren's S": 0.03311313666016608,
                    DP: 0.9606105366814504,
                    "DP norm": 0.9606105366814504,
                    "KL-divergence": 5.208495070263039,
                    DA: 0.00867507886435337,
                    X: 12.0,
                    Xpos: 0.15803215576067894,
                    Y: 0.03311313666016608,
                    Ypos: 0.10360933903068172,
                    Expected: 0.02879902189510588,
                    Residual: 0.0043141147650602035,
                    ColorScore: 0.5126129542813007,
                },
                s: NaN,
                os: 0,
                bg: 7.898329802725062e-7,
            }, {
                x: 0.0391510034100286,
                y: 0.1054056591907521,
                ox: 8,
                oy: 0.0336201976672986,
                term: "olabilece",
                cat25k: 98,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 8,
                ncat: 0,
                etc: {
                    Frequency: 8.0,
                    Range: 7.0,
                    SD: 0.08854647369952867,
                    VC: 14.045684390587734,
                    "Juilland's D": 0.6143457768794364,
                    "Rosengren's S": 0.0336201976672986,
                    DP: 0.9660265878877508,
                    "DP norm": 0.9660265878877508,
                    "KL-divergence": 4.909529226491893,
                    DA: 0.004140378548895929,
                    X: 8.0,
                    Xpos: 0.0391510034100286,
                    Y: 0.0336201976672986,
                    Ypos: 0.1054056591907521,
                    Expected: 0.020969598587433753,
                    Residual: 0.01265059907986485,
                    ColorScore: 0.5369859024422996,
                },
                s: NaN,
                os: 0,
                bg: 0.00784698381559588,
            }, {
                x: 0.1325206812656045,
                y: 0.09151162547242186,
                ox: 11,
                oy: 0.029698222683688966,
                term: "kat",
                cat25k: 135,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 11,
                ncat: 0,
                etc: {
                    Frequency: 11.0,
                    Range: 10.0,
                    SD: 0.10084219557476055,
                    VC: 11.633522380397377,
                    "Juilland's D": 0.6275178917403333,
                    "Rosengren's S": 0.029698222683688966,
                    DP: 0.9670113244707161,
                    "DP norm": 0.9670113244707161,
                    "KL-divergence": 5.238366491931662,
                    DA: 0.006452537998279495,
                    X: 11.0,
                    Xpos: 0.1325206812656045,
                    Y: 0.029698222683688966,
                    Ypos: 0.09151162547242186,
                    Expected: 0.021504079936589475,
                    Residual: 0.008194142747099491,
                    ColorScore: 0.5239567914791381,
                },
                s: NaN,
                os: 0,
                bg: 8.514567845044154e-6,
            }, {
                x: 0.15803215576067894,
                y: 0.14188943146838895,
                ox: 12,
                oy: 0.04391875063480923,
                term: "oldu",
                cat25k: 148,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 12,
                ncat: 0,
                etc: {
                    Frequency: 12.0,
                    Range: 12.0,
                    SD: 0.09678245621966297,
                    VC: 10.23474474522936,
                    "Juilland's D": 0.6915428512104156,
                    "Rosengren's S": 0.04391875063480923,
                    DP: 0.9542097488921786,
                    "DP norm": 0.9542097488921786,
                    "KL-divergence": 4.568929926565868,
                    DA: 0.00867507886435337,
                    X: 12.0,
                    Xpos: 0.15803215576067894,
                    Y: 0.04391875063480923,
                    Ypos: 0.14188943146838895,
                    Expected: 0.02879902189510588,
                    Residual: 0.015119728739703353,
                    ColorScore: 0.5442047691647087,
                },
                s: NaN,
                os: 0,
                bg: 0.011747430249632894,
            }, {
                x: 0.0391510034100286,
                y: 0.10072882981565295,
                ox: 8,
                oy: 0.032300033330317716,
                term: "unu",
                cat25k: 98,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 8,
                ncat: 0,
                etc: {
                    Frequency: 8.0,
                    Range: 8.0,
                    SD: 0.07914817670285086,
                    VC: 12.554879529489718,
                    "Juilland's D": 0.6270309477760507,
                    "Rosengren's S": 0.032300033330317716,
                    DP: 0.9665189561792291,
                    "DP norm": 0.9665189561792291,
                    "KL-divergence": 5.003011755900582,
                    DA: 0.0055205047318613865,
                    X: 8.0,
                    Xpos: 0.0391510034100286,
                    Y: 0.032300033330317716,
                    Ypos: 0.10072882981565295,
                    Expected: 0.020969598587433753,
                    Residual: 0.011330434742883963,
                    ColorScore: 0.5331262062281421,
                },
                s: NaN,
                os: 0,
                bg: 7.53767660540734e-5,
            }, {
                x: 0.33574935353791374,
                y: 0.13763441681711167,
                ox: 22,
                oy: 0.04271765516062843,
                term: "hen",
                cat25k: 271,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 22,
                ncat: 0,
                etc: {
                    Frequency: 22.0,
                    Range: 22.0,
                    SD: 0.1305217671303095,
                    VC: 7.528732840380124,
                    "Juilland's D": 0.76575997017583,
                    "Rosengren's S": 0.04271765516062843,
                    DP: 0.9527326440177352,
                    "DP norm": 0.9527326440177352,
                    "KL-divergence": 4.681126920984697,
                    DA: 0.016561514195583715,
                    X: 22.0,
                    Xpos: 0.33574935353791374,
                    Y: 0.04271765516062843,
                    Ypos: 0.13763441681711167,
                    Expected: 0.05228688039529833,
                    Residual: -0.009569225234669902,
                    ColorScore: 0.4720229509493179,
                },
                s: NaN,
                os: 0,
                bg: 1.178172953647463e-5,
            }, {
                x: 0.22345717505179155,
                y: 0.14309700428023753,
                ox: 15,
                oy: 0.04425962143266177,
                term: "arkada",
                cat25k: 185,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 15,
                ncat: 0,
                etc: {
                    Frequency: 15.0,
                    Range: 14.0,
                    SD: 0.11513754763012693,
                    VC: 9.740636529508738,
                    "Juilland's D": 0.6373894450172788,
                    "Rosengren's S": 0.04425962143266177,
                    DP: 0.9502708025603246,
                    "DP norm": 0.9502708025603246,
                    "KL-divergence": 4.6928258543714625,
                    DA: 0.009568874868559396,
                    X: 15.0,
                    Xpos: 0.22345717505179155,
                    Y: 0.04425962143266177,
                    Ypos: 0.14309700428023753,
                    Expected: 0.036184508831817654,
                    Residual: 0.00807511260084412,
                    ColorScore: 0.5236087891948746,
                },
                s: NaN,
                os: 0,
                bg: 0.014662756598240467,
            }, {
                x: 0.07368463583902007,
                y: 0.09663718634809502,
                ox: 9,
                oy: 0.03114505388756302,
                term: "yard",
                cat25k: 111,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 9,
                ncat: 0,
                etc: {
                    Frequency: 9.0,
                    Range: 9.0,
                    SD: 0.08391602529219312,
                    VC: 11.83215956619923,
                    "Juilland's D": 0.5858354351259656,
                    "Rosengren's S": 0.03114505388756302,
                    DP: 0.9640571147218251,
                    "DP norm": 0.9640571147218251,
                    "KL-divergence": 5.234661441370035,
                    DA: 0.006309148264984299,
                    X: 9.0,
                    Xpos: 0.07368463583902007,
                    Y: 0.03114505388756302,
                    Ypos: 0.09663718634809502,
                    Expected: 0.026809092001212464,
                    Residual: 0.004335961886350555,
                    ColorScore: 0.5126768275802323,
                },
                s: NaN,
                os: 0,
                bg: 1.1938213378717999e-6,
            }, {
                x: 0.0391510034100286,
                y: 0.07810537984850878,
                ox: 8,
                oy: 0.025913939369927714,
                term: "tan",
                cat25k: 98,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 8,
                ncat: 0,
                etc: {
                    Frequency: 8.0,
                    Range: 8.0,
                    SD: 0.07914817670285086,
                    VC: 12.554879529489718,
                    "Juilland's D": 0.5693285653028486,
                    "Rosengren's S": 0.025913939369927714,
                    DP: 0.9719350073855347,
                    "DP norm": 0.9719350073855347,
                    "KL-divergence": 5.411341672703783,
                    DA: 0.0055205047318613865,
                    X: 8.0,
                    Xpos: 0.0391510034100286,
                    Y: 0.025913939369927714,
                    Ypos: 0.07810537984850878,
                    Expected: 0.020969598587433753,
                    Residual: 0.0049443407824939604,
                    ColorScore: 0.5144555135032197,
                },
                s: NaN,
                os: 0,
                bg: 1.6410904430585205e-6,
            }, {
                x: 0.48014198038363837,
                y: 0.29416682866242044,
                ox: 36,
                oy: 0.08690325423337643,
                term: "proje",
                cat25k: 443,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 36,
                ncat: 0,
                etc: {
                    Frequency: 36.0,
                    Range: 36.0,
                    SD: 0.16602411220878902,
                    VC: 5.852349955359813,
                    "Juilland's D": 0.8007312207970757,
                    "Rosengren's S": 0.08690325423337643,
                    DP: 0.9010339734121212,
                    "DP norm": 0.9010339734121212,
                    "KL-divergence": 3.7105534558189737,
                    DA: 0.027602523659306044,
                    X: 36.0,
                    Xpos: 0.48014198038363837,
                    Y: 0.08690325423337643,
                    Ypos: 0.29416682866242044,
                    Expected: 0.07146581635466057,
                    Residual: 0.015437437878715862,
                    ColorScore: 0.5451336389475829,
                },
                s: NaN,
                os: 0,
                bg: 0.0009919268178436612,
            }, {
                x: 0.0391510034100286,
                y: 0.017175490991335675,
                ox: 8,
                oy: 0.0087147944206331,
                term: "imdilik",
                cat25k: 98,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 8,
                ncat: 0,
                etc: {
                    Frequency: 8.0,
                    Range: 8.0,
                    SD: 0.07914817670285086,
                    VC: 12.554879529489718,
                    "Juilland's D": 0.6419470810837042,
                    "Rosengren's S": 0.0087147944206331,
                    DP: 0.9911373707533357,
                    "DP norm": 0.9911373707533357,
                    "KL-divergence": 6.8629745242961535,
                    DA: 0.0055205047318613865,
                    X: 8.0,
                    Xpos: 0.0391510034100286,
                    Y: 0.0087147944206331,
                    Ypos: 0.017175490991335675,
                    Expected: 0.020969598587433753,
                    Residual: -0.012254804166800654,
                    ColorScore: 0.46417126268081704,
                },
                s: NaN,
                os: 0,
                bg: 0.00784698381559588,
            }, {
                x: 0.10457602270114133,
                y: 0.05620216834091554,
                ox: 10,
                oy: 0.01973115261879442,
                term: "farkl",
                cat25k: 123,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 10,
                ncat: 0,
                etc: {
                    Frequency: 10.0,
                    Range: 8.0,
                    SD: 0.10473877518482293,
                    VC: 13.29135057095403,
                    "Juilland's D": 0.540816645593033,
                    "Rosengren's S": 0.01973115261879442,
                    DP: 0.9773510585918352,
                    "DP norm": 0.9773510585918352,
                    "KL-divergence": 5.884608210513635,
                    DA: 0.004574132492113581,
                    X: 10.0,
                    Xpos: 0.10457602270114133,
                    Y: 0.01973115261879442,
                    Ypos: 0.05620216834091554,
                    Expected: 0.025393729342041836,
                    Residual: -0.005662576723247416,
                    ColorScore: 0.48344461721252313,
                },
                s: NaN,
                os: 0,
                bg: 0.009799118079372858,
            }, {
                x: 0.10457602270114133,
                y: 0.04996976945600075,
                ox: 10,
                oy: 0.017971885798946083,
                term: "cok",
                cat25k: 123,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 10,
                ncat: 0,
                etc: {
                    Frequency: 10.0,
                    Range: 10.0,
                    SD: 0.08842014911062773,
                    VC: 11.22051692213866,
                    "Juilland's D": 0.5894342747046865,
                    "Rosengren's S": 0.017971885798946083,
                    DP: 0.9798129000492493,
                    "DP norm": 0.9798129000492493,
                    "KL-divergence": 6.009822186986684,
                    DA: 0.007097791798107211,
                    X: 10.0,
                    Xpos: 0.10457602270114133,
                    Y: 0.017971885798946083,
                    Ypos: 0.04996976945600075,
                    Expected: 0.025393729342041836,
                    Residual: -0.007421843543095753,
                    ColorScore: 0.47830113977259303,
                },
                s: NaN,
                os: 0,
                bg: 0.00016738502740929826,
            }, {
                x: 0.22345717505179155,
                y: 0.11855248598126314,
                ox: 15,
                oy: 0.037331252846199516,
                term: "umar",
                cat25k: 185,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 15,
                ncat: 0,
                etc: {
                    Frequency: 15.0,
                    Range: 15.0,
                    SD: 0.1080768742379429,
                    VC: 9.14330356052997,
                    "Juilland's D": 0.6473111459988347,
                    "Rosengren's S": 0.037331252846199516,
                    DP: 0.9586410635155194,
                    "DP norm": 0.9586410635155194,
                    "KL-divergence": 4.91950440423234,
                    DA: 0.011041009463722329,
                    X: 15.0,
                    Xpos: 0.22345717505179155,
                    Y: 0.037331252846199516,
                    Ypos: 0.11855248598126314,
                    Expected: 0.036184508831817654,
                    Residual: 0.001146744014381862,
                    ColorScore: 0.5033526761835118,
                },
                s: NaN,
                os: 0,
                bg: 7.406877038434285e-5,
            }, {
                x: 0.07368463583902007,
                y: 0.06740714783058507,
                ox: 9,
                oy: 0.02289406773338537,
                term: "sosyal",
                cat25k: 111,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 9,
                ncat: 0,
                etc: {
                    Frequency: 9.0,
                    Range: 9.0,
                    SD: 0.08391602529219312,
                    VC: 11.83215956619923,
                    "Juilland's D": 0.5605885625936893,
                    "Rosengren's S": 0.02289406773338537,
                    DP: 0.9734121122599826,
                    "DP norm": 0.9734121122599826,
                    "KL-divergence": 5.698403345403748,
                    DA: 0.006309148264984299,
                    X: 9.0,
                    Xpos: 0.07368463583902007,
                    Y: 0.02289406773338537,
                    Ypos: 0.06740714783058507,
                    Expected: 0.026809092001212464,
                    Residual: -0.003915024267827093,
                    ColorScore: 0.4885538459708554,
                },
                s: NaN,
                os: 0,
                bg: 0.008823529411764706,
            }, {
                x: 0.07368463583902007,
                y: 0.04996666707757544,
                ox: 9,
                oy: 0.017971010066900196,
                term: "size",
                cat25k: 111,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 9,
                ncat: 0,
                etc: {
                    Frequency: 9.0,
                    Range: 9.0,
                    SD: 0.08391602529219312,
                    VC: 11.83215956619923,
                    "Juilland's D": 0.6308725703120281,
                    "Rosengren's S": 0.017971010066900196,
                    DP: 0.9803052683407314,
                    "DP norm": 0.9803052683407314,
                    "KL-divergence": 5.9206255676259705,
                    DA: 0.006309148264984299,
                    X: 9.0,
                    Xpos: 0.07368463583902007,
                    Y: 0.017971010066900196,
                    Ypos: 0.04996666707757544,
                    Expected: 0.026809092001212464,
                    Residual: -0.008838081934312268,
                    ColorScore: 0.4741605568134868,
                },
                s: NaN,
                os: 0,
                bg: 8.378086550502667e-8,
            }, {
                x: 0.20322867227230915,
                y: 0.020161685169917135,
                ox: 14,
                oy: 0.009557730252086135,
                term: "hay",
                cat25k: 172,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 14,
                ncat: 0,
                etc: {
                    Frequency: 14.0,
                    Range: 14.0,
                    SD: 0.10445380349648221,
                    VC: 9.46799118835971,
                    "Juilland's D": 0.7210991727243988,
                    "Rosengren's S": 0.009557730252086135,
                    DP: 0.990152634170369,
                    "DP norm": 0.990152634170369,
                    "KL-divergence": 6.75204817366712,
                    DA: 0.010252365930599416,
                    X: 14.0,
                    Xpos: 0.20322867227230915,
                    Y: 0.009557730252086135,
                    Ypos: 0.020161685169917135,
                    Expected: 0.03618450883181766,
                    Residual: -0.026626778579731523,
                    ColorScore: 0.4221526641793486,
                },
                s: NaN,
                os: 0,
                bg: 4.920526468214805e-6,
            }, {
                x: 0.18150043733463328,
                y: 0.101108664432084,
                ox: 13,
                oy: 0.03240725214767139,
                term: "olaca",
                cat25k: 160,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 13,
                ncat: 0,
                etc: {
                    Frequency: 13.0,
                    Range: 13.0,
                    SD: 0.10069429689496162,
                    VC: 9.829312519977409,
                    "Juilland's D": 0.696602118645858,
                    "Rosengren's S": 0.03240725214767139,
                    DP: 0.9650418513047874,
                    "DP norm": 0.9650418513047874,
                    "KL-divergence": 5.045442119621043,
                    DA: 0.009463722397476282,
                    X: 13.0,
                    Xpos: 0.18150043733463328,
                    Y: 0.03240725214767139,
                    Ypos: 0.101108664432084,
                    Expected: 0.03413316267301318,
                    Residual: -0.001725910525341788,
                    ColorScore: 0.49495404463366244,
                },
                s: NaN,
                os: 0,
                bg: 0.012720156555772993,
            }, {
                x: 0.0391510034100286,
                y: 0.010176487841547496,
                ox: 8,
                oy: 0.006739132361640113,
                term: "yoktur",
                cat25k: 98,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 8,
                ncat: 0,
                etc: {
                    Frequency: 8.0,
                    Range: 8.0,
                    SD: 0.07914817670285086,
                    VC: 12.554879529489718,
                    "Juilland's D": 0.6123242044548771,
                    "Rosengren's S": 0.006739132361640113,
                    DP: 0.9926144756277807,
                    "DP norm": 0.9926144756277807,
                    "KL-divergence": 7.341733899115865,
                    DA: 0.0055205047318613865,
                    X: 8.0,
                    Xpos: 0.0391510034100286,
                    Y: 0.006739132361640113,
                    Ypos: 0.010176487841547496,
                    Expected: 0.020969598587433753,
                    Residual: -0.014230466225793641,
                    ColorScore: 0.458395121668715,
                },
                s: NaN,
                os: 0,
                bg: 0.00784698381559588,
            }, {
                x: 0.15803215576067894,
                y: 0.0896921381937505,
                ox: 12,
                oy: 0.02918462211709968,
                term: "kullan",
                cat25k: 148,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 12,
                ncat: 0,
                etc: {
                    Frequency: 12.0,
                    Range: 12.0,
                    SD: 0.09678245621966297,
                    VC: 10.23474474522936,
                    "Juilland's D": 0.6166064374765532,
                    "Rosengren's S": 0.02918462211709968,
                    DP: 0.9650418513047866,
                    "DP norm": 0.9650418513047866,
                    "KL-divergence": 5.3817657918802,
                    DA: 0.00867507886435337,
                    X: 12.0,
                    Xpos: 0.15803215576067894,
                    Y: 0.02918462211709968,
                    Ypos: 0.0896921381937505,
                    Expected: 0.02879902189510588,
                    Residual: 0.00038560022199380165,
                    ColorScore: 0.5011273594319412,
                },
                s: NaN,
                os: 0,
                bg: 0.011747430249632894,
            }, {
                x: 0.0,
                y: 0.09388058986778955,
                ox: 7,
                oy: 0.030366928351463218,
                term: "ndan",
                cat25k: 86,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 7,
                ncat: 0,
                etc: {
                    Frequency: 7.0,
                    Range: 7.0,
                    SD: 0.07406569038618868,
                    VC: 13.427051585724776,
                    "Juilland's D": 0.591715937506236,
                    "Rosengren's S": 0.030366928351463218,
                    DP: 0.9684884293451623,
                    "DP norm": 0.9684884293451623,
                    "KL-divergence": 5.099381217469905,
                    DA: 0.004731861198738252,
                    X: 7.0,
                    Xpos: 0.0,
                    Y: 0.030366928351463218,
                    Ypos: 0.09388058986778955,
                    Expected: 0.022260856221882664,
                    Residual: 0.008106072129580554,
                    ColorScore: 0.5236993039683077,
                },
                s: NaN,
                os: 0,
                bg: 0.006869479882237487,
            }, {
                x: 0.0,
                y: 0.049100784423270115,
                ox: 7,
                oy: 0.017726590758744443,
                term: "projeyi",
                cat25k: 86,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 7,
                ncat: 0,
                etc: {
                    Frequency: 7.0,
                    Range: 7.0,
                    SD: 0.07406569038618868,
                    VC: 13.427051585724776,
                    "Juilland's D": 0.5699583272689073,
                    "Rosengren's S": 0.017726590758744443,
                    DP: 0.9783357951748034,
                    "DP norm": 0.9783357951748034,
                    "KL-divergence": 6.0760242557152075,
                    DA: 0.004731861198738252,
                    X: 7.0,
                    Xpos: 0.0,
                    Y: 0.017726590758744443,
                    Ypos: 0.049100784423270115,
                    Expected: 0.022260856221882664,
                    Residual: -0.004534265463138221,
                    ColorScore: 0.48674340250541637,
                },
                s: NaN,
                os: 0,
                bg: 0.006869479882237487,
            }, {
                x: 0.10457602270114133,
                y: 0.07156616352365967,
                ox: 10,
                oy: 0.02406806484864779,
                term: "bilgi",
                cat25k: 123,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 10,
                ncat: 0,
                etc: {
                    Frequency: 10.0,
                    Range: 8.0,
                    SD: 0.10473877518482293,
                    VC: 13.29135057095403,
                    "Juilland's D": 0.5161381213510706,
                    "Rosengren's S": 0.02406806484864779,
                    DP: 0.9709502708025655,
                    "DP norm": 0.9709502708025655,
                    "KL-divergence": 5.718430400736436,
                    DA: 0.004574132492113581,
                    X: 10.0,
                    Xpos: 0.10457602270114133,
                    Y: 0.02406806484864779,
                    Ypos: 0.07156616352365967,
                    Expected: 0.025393729342041836,
                    Residual: -0.001325664493394045,
                    ColorScore: 0.4961242232629179,
                },
                s: NaN,
                os: 0,
                bg: 0.0003247122237916646,
            }, {
                x: 0.0391510034100286,
                y: 0.08126521730333042,
                ox: 8,
                oy: 0.026805890814793832,
                term: "detayl",
                cat25k: 98,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 8,
                ncat: 0,
                etc: {
                    Frequency: 8.0,
                    Range: 7.0,
                    SD: 0.08854647369952867,
                    VC: 14.045684390587734,
                    "Juilland's D": 0.4299194340433662,
                    "Rosengren's S": 0.026805890814793832,
                    DP: 0.9709502708025682,
                    "DP norm": 0.9709502708025682,
                    "KL-divergence": 5.399293605650741,
                    DA: 0.004140378548895929,
                    X: 8.0,
                    Xpos: 0.0391510034100286,
                    Y: 0.026805890814793832,
                    Ypos: 0.08126521730333042,
                    Expected: 0.020969598587433753,
                    Residual: 0.0058362922273600785,
                    ColorScore: 0.5170632658250519,
                },
                s: NaN,
                os: 0,
                bg: 0.00784698381559588,
            }, {
                x: 0.07368463583902007,
                y: 0.10816704014711717,
                ox: 9,
                oy: 0.03439967375398694,
                term: "mas",
                cat25k: 111,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 9,
                ncat: 0,
                etc: {
                    Frequency: 9.0,
                    Range: 8.0,
                    SD: 0.09283287903580076,
                    VC: 13.089435944047906,
                    "Juilland's D": 0.6161022535868614,
                    "Rosengren's S": 0.03439967375398694,
                    DP: 0.9635647464303392,
                    "DP norm": 0.9635647464303392,
                    "KL-divergence": 4.939726473663534,
                    DA: 0.004907115317209998,
                    X: 9.0,
                    Xpos: 0.07368463583902007,
                    Y: 0.03439967375398694,
                    Ypos: 0.10816704014711717,
                    Expected: 0.026809092001212464,
                    Residual: 0.007590581752774477,
                    ColorScore: 0.5221921914065919,
                },
                s: NaN,
                os: 0,
                bg: 2.7255630559012982e-6,
            }, {
                x: 0.0391510034100286,
                y: 0.05534579176454509,
                ox: 8,
                oy: 0.019489416663839663,
                term: "konusunda",
                cat25k: 98,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 8,
                ncat: 0,
                etc: {
                    Frequency: 8.0,
                    Range: 5.0,
                    SD: 0.10484543987743368,
                    VC: 16.631107900557918,
                    "Juilland's D": 0.5114315502273308,
                    "Rosengren's S": 0.019489416663839663,
                    DP: 0.978828163466278,
                    "DP norm": 0.978828163466278,
                    "KL-divergence": 5.781538967495749,
                    DA: 0.002563091482649993,
                    X: 8.0,
                    Xpos: 0.0391510034100286,
                    Y: 0.019489416663839663,
                    Ypos: 0.05534579176454509,
                    Expected: 0.020969598587433753,
                    Residual: -0.0014801819235940906,
                    ColorScore: 0.49567246864142256,
                },
                s: NaN,
                os: 0,
                bg: 0.00784698381559588,
            }, {
                x: 0.1325206812656045,
                y: 0.01954385743837633,
                ox: 11,
                oy: 0.00938333130096753,
                term: "binance",
                cat25k: 135,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 11,
                ncat: 0,
                etc: {
                    Frequency: 11.0,
                    Range: 11.0,
                    SD: 0.09269899826374953,
                    VC: 10.694093526972559,
                    "Juilland's D": 0.671795480909922,
                    "Rosengren's S": 0.00938333130096753,
                    DP: 0.9896602658788874,
                    "DP norm": 0.9896602658788874,
                    "KL-divergence": 6.862913078850915,
                    DA: 0.007886435331230235,
                    X: 11.0,
                    Xpos: 0.1325206812656045,
                    Y: 0.00938333130096753,
                    Ypos: 0.01954385743837633,
                    Expected: 0.021504079936589475,
                    Residual: -0.012120748635621945,
                    ColorScore: 0.46456319390610723,
                },
                s: NaN,
                os: 0,
                bg: 0.010773751224289911,
            }, {
                x: 0.0,
                y: 0.0,
                ox: 7,
                oy: 0.0038665374374676183,
                term: "guzel",
                cat25k: 86,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 7,
                ncat: 0,
                etc: {
                    Frequency: 7.0,
                    Range: 7.0,
                    SD: 0.07406569038618868,
                    VC: 13.427051585724776,
                    "Juilland's D": 0.6162591840913166,
                    "Rosengren's S": 0.0038665374374676183,
                    DP: 0.9960610536681535,
                    "DP norm": 0.9960610536681535,
                    "KL-divergence": 8.037762459381405,
                    DA: 0.004731861198738252,
                    X: 7.0,
                    Xpos: 0.0,
                    Y: 0.0038665374374676183,
                    Ypos: 0.0,
                    Expected: 0.022260856221882664,
                    Residual: -0.018394318784415047,
                    ColorScore: 0.44622148123121125,
                },
                s: NaN,
                os: 0,
                bg: 0.006869479882237487,
            }, {
                x: 0.0391510034100286,
                y: 0.06141070565500878,
                ox: 8,
                oy: 0.021201406215496214,
                term: "tak",
                cat25k: 98,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 8,
                ncat: 0,
                etc: {
                    Frequency: 8.0,
                    Range: 8.0,
                    SD: 0.07914817670285086,
                    VC: 12.554879529489718,
                    "Juilland's D": 0.6297536683633793,
                    "Rosengren's S": 0.021201406215496214,
                    DP: 0.9783357951747984,
                    "DP norm": 0.9783357951747984,
                    "KL-divergence": 5.592292445608846,
                    DA: 0.0055205047318613865,
                    X: 8.0,
                    Xpos: 0.0391510034100286,
                    Y: 0.021201406215496214,
                    Ypos: 0.06141070565500878,
                    Expected: 0.020969598587433753,
                    Residual: 0.00023180762806246022,
                    ColorScore: 0.5006777239767677,
                },
                s: NaN,
                os: 0,
                bg: 1.129640350753329e-5,
            }, {
                x: 0.0391510034100286,
                y: 0.034123966106428844,
                ox: 8,
                oy: 0.013498969899063875,
                term: "rler",
                cat25k: 98,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 8,
                ncat: 0,
                etc: {
                    Frequency: 8.0,
                    Range: 8.0,
                    SD: 0.07914817670285086,
                    VC: 12.554879529489718,
                    "Juilland's D": 0.6155966691854441,
                    "Rosengren's S": 0.013498969899063875,
                    DP: 0.9842442146725863,
                    "DP norm": 0.9842442146725863,
                    "KL-divergence": 6.407492500574314,
                    DA: 0.0055205047318613865,
                    X: 8.0,
                    Xpos: 0.0391510034100286,
                    Y: 0.013498969899063875,
                    Ypos: 0.034123966106428844,
                    Expected: 0.020969598587433753,
                    Residual: -0.0074706286883698785,
                    ColorScore: 0.4781585091657458,
                },
                s: NaN,
                os: 0,
                bg: 0.00784698381559588,
            }, {
                x: 0.1325206812656045,
                y: 0.05797452050138077,
                ox: 11,
                oy: 0.02023144799567411,
                term: "bilmiyorum",
                cat25k: 135,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 11,
                ncat: 0,
                etc: {
                    Frequency: 11.0,
                    Range: 11.0,
                    SD: 0.09269899826374953,
                    VC: 10.694093526972559,
                    "Juilland's D": 0.6277190372853276,
                    "Rosengren's S": 0.02023144799567411,
                    DP: 0.9734121122599827,
                    "DP norm": 0.9734121122599827,
                    "KL-divergence": 6.059063047631478,
                    DA: 0.007886435331230235,
                    X: 11.0,
                    Xpos: 0.1325206812656045,
                    Y: 0.02023144799567411,
                    Ypos: 0.05797452050138077,
                    Expected: 0.021504079936589475,
                    Residual: -0.0012726319409153662,
                    ColorScore: 0.4962792717946008,
                },
                s: NaN,
                os: 0,
                bg: 0.010773751224289911,
            }, {
                x: 0.15803215576067894,
                y: 0.03187557770522466,
                ox: 12,
                oy: 0.012864300137803169,
                term: "buluyorum",
                cat25k: 148,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 12,
                ncat: 0,
                etc: {
                    Frequency: 12.0,
                    Range: 12.0,
                    SD: 0.09678245621966297,
                    VC: 10.23474474522936,
                    "Juilland's D": 0.6765512262671773,
                    "Rosengren's S": 0.012864300137803169,
                    DP: 0.984244214672586,
                    "DP norm": 0.984244214672586,
                    "KL-divergence": 6.520931815181567,
                    DA: 0.00867507886435337,
                    X: 12.0,
                    Xpos: 0.15803215576067894,
                    Y: 0.012864300137803169,
                    Ypos: 0.03187557770522466,
                    Expected: 0.02879902189510588,
                    Residual: -0.015934721757302713,
                    ColorScore: 0.4534124778881948,
                },
                s: NaN,
                os: 0,
                bg: 0.011747430249632894,
            }, {
                x: 0.0,
                y: 0.05563358718298387,
                ox: 7,
                oy: 0.01957065487402374,
                term: "olan",
                cat25k: 86,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 7,
                ncat: 0,
                etc: {
                    Frequency: 7.0,
                    Range: 7.0,
                    SD: 0.07406569038618868,
                    VC: 13.427051585724776,
                    "Juilland's D": 0.5953217717697543,
                    "Rosengren's S": 0.01957065487402374,
                    DP: 0.9798129000492466,
                    "DP norm": 0.9798129000492466,
                    "KL-divergence": 5.723523552976211,
                    DA: 0.004731861198738252,
                    X: 7.0,
                    Xpos: 0.0,
                    Y: 0.01957065487402374,
                    Ypos: 0.05563358718298387,
                    Expected: 0.022260856221882664,
                    Residual: -0.0026902013478589254,
                    ColorScore: 0.49213479741363236,
                },
                s: NaN,
                os: 0,
                bg: 9.887773767736194e-5,
            }, {
                x: 0.18150043733463328,
                y: 0.2376219449473378,
                ox: 13,
                oy: 0.07094189816662853,
                term: "hakk",
                cat25k: 160,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 13,
                ncat: 0,
                etc: {
                    Frequency: 13.0,
                    Range: 13.0,
                    SD: 0.10069429689496162,
                    VC: 9.829312519977409,
                    "Juilland's D": 0.7174346145475105,
                    "Rosengren's S": 0.07094189816662853,
                    DP: 0.9281142294436322,
                    "DP norm": 0.9281142294436322,
                    "KL-divergence": 3.835935409068133,
                    DA: 0.009463722397476282,
                    X: 13.0,
                    Xpos: 0.18150043733463328,
                    Y: 0.07094189816662853,
                    Ypos: 0.2376219449473378,
                    Expected: 0.03413316267301318,
                    Residual: 0.03680873549361535,
                    ColorScore: 0.6076157968011277,
                },
                s: NaN,
                os: 0,
                bg: 0.012720156555772993,
            }, {
                x: 0.0,
                y: 0.06388963547956311,
                ox: 7,
                oy: 0.02190115266459252,
                term: "geni",
                cat25k: 86,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 7,
                ncat: 0,
                etc: {
                    Frequency: 7.0,
                    Range: 7.0,
                    SD: 0.07406569038618868,
                    VC: 13.427051585724776,
                    "Juilland's D": 0.584392356418239,
                    "Rosengren's S": 0.02190115266459252,
                    DP: 0.9768586903003518,
                    "DP norm": 0.9768586903003518,
                    "KL-divergence": 5.595657101517393,
                    DA: 0.004731861198738252,
                    X: 7.0,
                    Xpos: 0.0,
                    Y: 0.02190115266459252,
                    Ypos: 0.06388963547956311,
                    Expected: 0.022260856221882664,
                    Residual: -0.000359703557290144,
                    ColorScore: 0.4989483533076899,
                },
                s: NaN,
                os: 0,
                bg: 0.0001284003154979181,
            }, {
                x: 0.0,
                y: 0.0812563612326717,
                ox: 7,
                oy: 0.026803390944109717,
                term: "elimden",
                cat25k: 86,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 7,
                ncat: 0,
                etc: {
                    Frequency: 7.0,
                    Range: 7.0,
                    SD: 0.07406569038618868,
                    VC: 13.427051585724776,
                    "Juilland's D": 0.557282483904011,
                    "Rosengren's S": 0.026803390944109717,
                    DP: 0.9704579025110878,
                    "DP norm": 0.9704579025110878,
                    "KL-divergence": 5.364984266643791,
                    DA: 0.004731861198738252,
                    X: 7.0,
                    Xpos: 0.0,
                    Y: 0.026803390944109717,
                    Ypos: 0.0812563612326717,
                    Expected: 0.022260856221882664,
                    Residual: 0.004542534722227053,
                    ColorScore: 0.5132807738998273,
                },
                s: NaN,
                os: 0,
                bg: 0.006869479882237487,
            }, {
                x: 0.0391510034100286,
                y: 0.08697156528872708,
                ox: 8,
                oy: 0.028416665230647675,
                term: "inin",
                cat25k: 98,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 8,
                ncat: 0,
                etc: {
                    Frequency: 8.0,
                    Range: 8.0,
                    SD: 0.07914817670285086,
                    VC: 12.554879529489718,
                    "Juilland's D": 0.5613816503347485,
                    "Rosengren's S": 0.028416665230647675,
                    DP: 0.9684884293451579,
                    "DP norm": 0.9684884293451579,
                    "KL-divergence": 5.315971572366388,
                    DA: 0.0055205047318613865,
                    X: 8.0,
                    Xpos: 0.0391510034100286,
                    Y: 0.028416665230647675,
                    Ypos: 0.08697156528872708,
                    Expected: 0.020969598587433753,
                    Residual: 0.007447066643213922,
                    ColorScore: 0.5217726037010855,
                },
                s: NaN,
                os: 0,
                bg: 0.0003724048040219719,
            }, {
                x: 0.0391510034100286,
                y: 0.09090248985642924,
                ox: 8,
                oy: 0.029526277322393567,
                term: "lmas",
                cat25k: 98,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 8,
                ncat: 0,
                etc: {
                    Frequency: 8.0,
                    Range: 8.0,
                    SD: 0.07914817670285086,
                    VC: 12.554879529489718,
                    "Juilland's D": 0.6338612253967354,
                    "Rosengren's S": 0.029526277322393567,
                    DP: 0.9699655342196043,
                    "DP norm": 0.9699655342196043,
                    "KL-divergence": 5.107649539082038,
                    DA: 0.0055205047318613865,
                    X: 8.0,
                    Xpos: 0.0391510034100286,
                    Y: 0.029526277322393567,
                    Ypos: 0.09090248985642924,
                    Expected: 0.020969598587433753,
                    Residual: 0.008556678734959813,
                    ColorScore: 0.525016719202258,
                },
                s: NaN,
                os: 0,
                bg: 0.00784698381559588,
            }, {
                x: 0.1325206812656045,
                y: 0.1599418672325837,
                ox: 11,
                oy: 0.04901454951479788,
                term: "ini",
                cat25k: 135,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 11,
                ncat: 0,
                etc: {
                    Frequency: 11.0,
                    Range: 11.0,
                    SD: 0.09269899826374953,
                    VC: 10.694093526972559,
                    "Juilland's D": 0.6718325944790189,
                    "Rosengren's S": 0.04901454951479788,
                    DP: 0.9492860659773623,
                    "DP norm": 0.9492860659773623,
                    "KL-divergence": 4.404494907786103,
                    DA: 0.007886435331230235,
                    X: 11.0,
                    Xpos: 0.1325206812656045,
                    Y: 0.04901454951479788,
                    Ypos: 0.1599418672325837,
                    Expected: 0.021504079936589475,
                    Residual: 0.027510469578208407,
                    ColorScore: 0.5804309375024742,
                },
                s: NaN,
                os: 0,
                bg: 1.5052420052833995e-5,
            }, {
                x: 0.0391510034100286,
                y: 0.04739243307716099,
                ox: 8,
                oy: 0.01724436138040225,
                term: "dusunuyorum",
                cat25k: 98,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 8,
                ncat: 0,
                etc: {
                    Frequency: 8.0,
                    Range: 7.0,
                    SD: 0.08854647369952867,
                    VC: 14.045684390587734,
                    "Juilland's D": 0.5078431704426329,
                    "Rosengren's S": 0.01724436138040225,
                    DP: 0.9807976366322111,
                    "DP norm": 0.9807976366322111,
                    "KL-divergence": 6.032492500574312,
                    DA: 0.004140378548895929,
                    X: 8.0,
                    Xpos: 0.0391510034100286,
                    Y: 0.01724436138040225,
                    Ypos: 0.04739243307716099,
                    Expected: 0.020969598587433753,
                    Residual: -0.0037252372070315024,
                    ColorScore: 0.48910871658773936,
                },
                s: NaN,
                os: 0,
                bg: 0.00784698381559588,
            }, {
                x: 0.07368463583902007,
                y: 0.08781944241356221,
                ox: 9,
                oy: 0.028656001980521192,
                term: "fikir",
                cat25k: 111,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 9,
                ncat: 0,
                etc: {
                    Frequency: 9.0,
                    Range: 9.0,
                    SD: 0.08391602529219312,
                    VC: 11.83215956619923,
                    "Juilland's D": 0.6464021457925611,
                    "Rosengren's S": 0.028656001980521192,
                    DP: 0.9694731659281214,
                    "DP norm": 0.9694731659281214,
                    "KL-divergence": 5.205165758789109,
                    DA: 0.006309148264984299,
                    X: 9.0,
                    Xpos: 0.07368463583902007,
                    Y: 0.028656001980521192,
                    Ypos: 0.08781944241356221,
                    Expected: 0.026809092001212464,
                    Residual: 0.0018469099793087286,
                    ColorScore: 0.5053997152137361,
                },
                s: NaN,
                os: 0,
                bg: 0.008823529411764706,
            }, {
                x: 0.20322867227230915,
                y: 0.18622956055530865,
                ox: 14,
                oy: 0.05643497742498146,
                term: "isterim",
                cat25k: 172,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 14,
                ncat: 0,
                etc: {
                    Frequency: 14.0,
                    Range: 13.0,
                    SD: 0.11174364050860945,
                    VC: 10.12876284324467,
                    "Juilland's D": 0.703795868082081,
                    "Rosengren's S": 0.05643497742498146,
                    DP: 0.9414081733136488,
                    "DP norm": 0.9414081733136488,
                    "KL-divergence": 4.202095858375813,
                    DA: 0.008787742226228135,
                    X: 14.0,
                    Xpos: 0.20322867227230915,
                    Y: 0.05643497742498146,
                    Ypos: 0.18622956055530865,
                    Expected: 0.03618450883181766,
                    Residual: 0.020250468593163796,
                    ColorScore: 0.5592052479941219,
                },
                s: NaN,
                os: 0,
                bg: 0.013691931540342298,
            }, {
                x: 0.0391510034100286,
                y: 0.07610808436663939,
                ox: 8,
                oy: 0.02535014752419224,
                term: "pek",
                cat25k: 98,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 8,
                ncat: 0,
                etc: {
                    Frequency: 8.0,
                    Range: 7.0,
                    SD: 0.08854647369952867,
                    VC: 14.045684390587734,
                    "Juilland's D": 0.43793555483669566,
                    "Rosengren's S": 0.02535014752419224,
                    DP: 0.9724273756770185,
                    "DP norm": 0.9724273756770185,
                    "KL-divergence": 5.4755072510328455,
                    DA: 0.004140378548895929,
                    X: 8.0,
                    Xpos: 0.0391510034100286,
                    Y: 0.02535014752419224,
                    Ypos: 0.07610808436663939,
                    Expected: 0.020969598587433753,
                    Residual: 0.004380548936758488,
                    ColorScore: 0.5128071844341777,
                },
                s: NaN,
                os: 0,
                bg: 0.00014703855167026608,
            }, {
                x: 0.0,
                y: 0.09875907135932317,
                ox: 7,
                oy: 0.031744014571036386,
                term: "bulunmak",
                cat25k: 86,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 7,
                ncat: 0,
                etc: {
                    Frequency: 7.0,
                    Range: 7.0,
                    SD: 0.07406569038618868,
                    VC: 13.427051585724776,
                    "Juilland's D": 0.5534538605977014,
                    "Rosengren's S": 0.031744014571036386,
                    DP: 0.9665189561792343,
                    "DP norm": 0.9665189561792343,
                    "KL-divergence": 5.063963001263678,
                    DA: 0.004731861198738252,
                    X: 7.0,
                    Xpos: 0.0,
                    Y: 0.031744014571036386,
                    Ypos: 0.09875907135932317,
                    Expected: 0.022260856221882664,
                    Residual: 0.009483158349153722,
                    ColorScore: 0.527725419747507,
                },
                s: NaN,
                os: 0,
                bg: 0.006869479882237487,
            }, {
                x: 0.0,
                y: 0.10944929242744987,
                ox: 7,
                oy: 0.03476162489561305,
                term: "payla",
                cat25k: 86,
                ncat25k: 0,
                neut25k: 0,
                neut: 0,
                extra25k: 0,
                extra: 0,
                cat: 7,
                ncat: 0,
                etc: {
                    Frequency: 7.0,
                    Range: 7.0,
                    SD: 0.07406569038618868,
                    VC: 13.427051585724776,
                    "Juilland's D": 0.5394828075645604,
                    "Rosengren's S": 0.03476162489561305,
                    DP: 0.9630723781388532,
                    "DP norm": 0.9630723781388532,
                    "KL-divergence": 4.952775999670348,
                    DA: 0.004731861198738252,
                    X: 7.0,
                    Xpos: 0.0,
                    Y: 0.03476162489561305,
                    Ypos: 0.10944929242744987,
                    Expected: 0.022260856221882664,
                    Residual: 0.012500768673730383,
                    ColorScore: 0.5365478510307266,
                },
                s: NaN,
                os: 0,
                bg: 0.006869479882237487,
            }, ],
            docs: {
                categories: ["_"],
                labels: [
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0,
                ],
                texts: ["Geli  meli",
                    "Ben  yeniyim  sadece  arkadasimin  onerisiyle  buldum  sizi  Gelecegin  cryphto  valute  dogru  gittigini  gordugum  icin  ben  merak  duyuyorum  Bilgim  oldugu  icin  yapacagima  dair  bir  fikrim  yok  ama  hizli  ogrenen  birisi  oldugumu  biliyorum",
                    "Para  kazanmak  geldim", "",
                    "Ben  yeniyim  sadece  arkadasimin  onerisiyle  buldum  sizi  Gelecegin  cryphto  valute  dogru  gittigini  gordugum  icin  ben  merak  duyuyorum  Bilgim  oldugu  icin  yapacagima  dair  bir  fikrim  yok  ama  hizli  ogrenen  birisi  oldugumu  biliyorum",
                    "Para  kazanmak  geldim", "FxTorikul", "Nothing", "Nothing", "", "Yok",
                    "Galiba  sadece  yayabilirim", "Yes",
                    "Yes  can  learn  very  fast  what  TFB  and  try  myself  best  invest  this  contact",
                    "think  truefeedback  will  most  have  many  user  everyday  have  more  event",
                    "Crypto  Investor", "like  History  will  good  TFB  can  preare  articles  about  that",
                    "like  History  will  good  TFB  can  preare  articles  about  that", "perfect",
                    "name  zahra  and  love  cryptocurency", "good  for  all  like", "allah  iyi  yerlere  gelece",
                    "etc",
                    "was  Biomedical  Engineer  and  Community  Health  Worker  With  over  years  vast  Working  Experience  covering  various  fields  Professional  Carrier  has  led  gain  complex  experience  especially  HealthCare  Medical  Field  nationally  and  internationally  with  multimanagement  skills  some  Technical  Business  and  Administrative  sectors",
                    "was  Biomedical  Engineer  and  Community  Health  Worker  With  over  years  vast  Working  Experience  covering  various  fields  Professional  Carrier  has  led  gain  complex  experience  especially  HealthCare  Medical  Field  nationally  and  internationally  with  multimanagement  skills  some  Technical  Business  and  Administrative  sectors",
                    "manuelextremo", "manuelextremo",
                    "young  man  who  getting  know  more  about  crypto  currency  can  contribute  promoting  TFB  all  social  media  accounts  address  username  Abymac",
                    "Creating  awareness  for  the  program", "Tradewithchrisnet", "Anderbby",
                    "can  help  publicize  and  market  your  platform  through  article  writng  You  can  contact  Petozz",
                    "with  great  team  support  believe  TFB  will  the  largest  community  very  soon  Oluwatosin  and",
                    "Muhammad  sani  nasiru",
                    "believe  can  contribute  greatly  TFB  with  the  ideas  and  experience  have  heard  cryptocurrency",
                    "Ogundeji  Mayowa  years  old  and  graduate  willing  learn  everyday  and  believe  with  TFB  support  will  contribute  massively  this  great  project  username  bringjoy  and  address",
                    "", "Yes  believe  can  contribute  TFB  with  great  ideas",
                    "charmonenterprise  twitter  LinkedIn  victormondaycharlie  youtube  advertisehub  Instagram  charmonenterprise  Facebook  All  about  and  work  visible  this  social  handles  lover  crypto  ready  get  involved  with  many  projects  possible",
                    "can  bring  multiple  people  because  have  access  the  public", "down  handle",
                    "guy  with  strict  aim  goals  mannysam",
                    "name  Benjamin  Ntoe  forex  trader  and  crypto  enthusiast  also  design  animations  and  Nigerian  who  passion  driven  nMy  mission  generally  life  not  merely  survive  but  thrive  and  with  some  passion  compassion  humor  and  some  style  happy  here  plan  contribute  little  way  this  community  nThank  you  everyone",
                    "hardthey  twitter  Lord  Pemi",
                    "cryptocurrency  writer  https  cryptostocksreviews  org  write  educative  reviews  and  blogs  crypto  Reach  https",
                    "Yes", "Muhammad  sani  nasiru",
                    "Amusat  Yusuff  and  professional  content  writer  There  are  different  ways  can  use  skills  contribute  the  development  TFB  can  refer  people  use  the  app  using  the  referral  program  address  and  star  hamzat  phone  number  for  WhatsApp",
                    "name  Israel  Udensi  was  designer  for  Bitmama  Nigerian  based  wallet  system  believe  would  able  add  few  things  the  TFB  system  when  comes  design",
                    "very  hard  working  young  teenager  who  always  ready  keep  the  rules  and  regulations  and  always  ready  make  sure  work  the  very  support  this  forum  Instagram  name  skyez  noble",
                    "TFB  great", "", "will  willing  contribute  the  greatness  these  company",
                    "thought  that  real  app  and  help  earn  money  online", "Take  moon",
                    "thought  that  real  app  and  help  earn  money  online", "Jnn", "Jnn", "", "",
                    "Mining  olmas  faydal", "", "", "", "", "Telwgram", "Yok", "Tfb  nice", "ozdemir",
                    "Gelece  kripto  paras  olarak  yorum  zden", "Yok", "Daha  fazla  puan", "Olabilir",
                    "endustri  muhendisiyim  projeye  katki  sunabilecek  operasyonlarda  yer  almak  istiyorum",
                    "Yok", "earn  many  money", "", "Facebook", "katk  bulunmaya  aca",
                    "ile  ula  abilirsiniz  ismail  dikici  projenin  geli  yece  ine  inanc  tam  bende  destek  olmak  istiyorum",
                    "", "", "Dogan", "", "Evet", "Daha  puan  vermeli", "lar",
                    "renciyim  kendimi  geli  tirmek  imkan  olu  turmaya  yorum  Bir  yat  yakla  yla  uzun  vade  portf  mde  tutaca",
                    "kripto  paralara  kar  merak  fazla  her  onlar  inceleyerek  iriyorum", "fazla  zaman",
                    "Yeni  Bir  Kripto  Para  kararak  nce  Madencili  Daha  Sonra  Borsaya  Girmeye  abilirsiniz",
                    "Ankara  lar", "Whatsapp", "",
                    "Futbol  plerinin  derneklerineklerine  yap  lan  demeleri  aidat  demeleri  TFB  zerinden  kripto  para  demesi  ile  yap  labilir",
                    "", "zel", "gelecek  vaat  eden  bir  projedir", "",
                    "Reklam  ajans  nda  neticiyim  Projenin  biraz  daha  hype  olmas  gerekiyor  Twitter  instagram  daha  aktif  olmak  gerekiyor  evremizdek  herkes  neredeyse  kripto  borsas  ilgi  duyuyor  Kolay  para  kazan  yor  herkes",
                    "", "stagram", "PARA  KAZANMAK  YORUM", "zel", "",
                    "zel  bir  uygulama  test  ettikten  sonra  daha  net  klama  yapabilirim",
                    "veri  pos  sistemleri  ile  malar  olabilir", "Naim  kara", "Yok", "ekk  ederim",
                    "Uygulaman  endim  burda  hem  leniyorum  hem  haberlerden  yeni  eyler  reniyorum", "", "",
                    "Jdjwjaj", "", "jiyaneugur", "",
                    "Uygulamay  kullanarak  hem  kend  hem  uygulamaya  kazand  rmk", "aminekocyigitgmail", "",
                    "projeye  katk  bulunaca  inan  yorum", "nssanlara  biraz  faydal  ler  yaparsan", "",
                    "nstagram", "uan  akl  gelen  bir  yok", "", "Bfkb", "Gelecek  vaad  ediyor",
                    "Daha  reklam  yapilmasi", "", "uan  ama  ilerde  ncelerimi  ylemek  isterlm",
                    "Bende  kazanmak  istiyorum", "", "zel",
                    "yok  ama  ilerleyen  zamanlarda  rekli  feedback  verilebilecek  bir  olmas  iyi  olur", "",
                    "", "", "colpan  onur", "ederim", "", "Tfb  projesi  ile  ilgili  hedeflerim  var",
                    "Tbf  projesine  faydal  olabilece  demek  mant  geldi  bana  yanl  renmediysem  anket  platformu  Kat  lan  herkesin  bir  faydas  olacakt  ancak  kat  lanlar  yleyip  ylemediklerinden  emin  olamayaca  sorulan  sorulara  nsanlar  yalan  ylemeye  gerek  rmeyece  sorular  sorulursa  ruluk  pay  artar  ama  yine  kesin  diyemeyiz  eride  neler  oldu  unu  bilmeden  kesin  bir  yarg  varmak  faydal  olabilece  imi  uan  daha  giri  nda  iddia  etmem  kadar  tatmin  edici  olabilir  Neyse  bakal  neler  oluyor  eride",
                    "projeye  yap  lacak  her  etkinliklere  kat  larak  destekleyece",
                    "Sonuna  kadar  arkan  zday", "Berkekbskl", "", "Hen  yok", "",
                    "yat  arkada  lar  kurdu  tfb  projesinin  yerlere  gelece  ine  inan  yorum  onlara  yard  olmak  uugulamay  arkada  evreme  tan  yorum",
                    "Hen  yok", "", "", "", "yid  ins  kazand", "Yok", "savasalmz", "Harika", "zel  bir  proje", "",
                    "", "imdilik  yok",
                    "Bana  nodan  ula  abilirsin  kazanmak  dostlar  maza  kazand  rmaya  yoruz", "Yok", "Severin",
                    "", "", "Farkl  fikirlerim  var", "ksek  kazan  lar  elde  etmeyi  hedefliyoruz", "Var", "",
                    "Sldkfk", "SafiyeSularoglu", "Yok", "Yeniyim  hen  takipte  kalaca", "",
                    "Daha  cok  tfb  kazanmak  icin  uygulama  cogaltiniz", "", "Umar  olur",
                    "Sosyal  medya  zerinden  yay  laml", "", "",
                    "Wyrexia  adl  instagram  sayfamda  reklam  yapmak  istedim  ama  yetkilileriniz  ilk  reklama  cak  bak  coin  istedi  imde  att  lar",
                    "Daha  borsada  listelenmeniz  bir  nce", "buradan  ula  fikirlerimi  size  sunacagim", "Hay",
                    "zel  olaca  yorum", "", "gayet  yla  tasarlanm  bir  proje  tebrik  ederim", "", "Yok", "",
                    "Uzun  vadeli  bir  yat", "", "", "", "zel", "Yok", "yok", "", "tamam",
                    "malesef  yok  ama  ihtiyac  olursa  yard  etmek  ula  abilirsiniz", "Okey", "yok",
                    "Cok  iyi  bir  proje", "", "Yok",
                    "Merhaba  tfb  kaz  yapmamiza  izin  verin  bana  geri  bildirim  atin  ben  size  tam  olarak  nasil  bisey  olacagini  anlatim",
                    "Yok", "Evet", "yoktur", "malesrf", "brahimniturbil", "Mesleki  evremde  destek  olabilirim",
                    "", "Hayir", "Have  good  work",
                    "adresim  tfb  projelerine  kat  larak  destekte  bulunmay  yorum", "yok", "Fikrim  yok", "",
                    "bir  yak  evrem  var  tfb  uygulamas  katk  lar", "nanmak  arman  yar  Bunun  buraday", "", "",
                    "kullan  Ahmetozt  tek  iste  site  uzun  vadeli  olsun", "", "Supet",
                    "ben  mecit  Erva  nday  internetten  para  kazanmay  ara  rken  uygulamaya  rastlad  umar  para  kazan",
                    "olabilir  diye  yorum", "WhatsApp", "Karaman  sar  veliler  dumlug  cami  mahallesi",
                    "Hen  yok", "", "yok",
                    "Tfb  uygulamasinin  sosyal  medyada  daha  dikkat  ekmesi  para  kazanacaklar  sterecek  reklamlarla  yay  nlanmas  gerekir",
                    "kullan  kaya", "", "stemiyom", "ikta", "", "Whatsapp", "",
                    "Hepinize  iyi  calismalar  diliyorum", "", "Yeniyim  ama  katk  layaca  ndan  phem  yok",
                    "Hay", "Bar  han  kele", "",
                    "esangle  projesi  olmas  gurur  verici  zamanlar  mda  hem  oyun  oynay  anketlere  kat  hem  kazan  lamak  uma  gidecektir",
                    "zel  yat  mant", "", "", "",
                    "Tfb  nin  uzun  vadede  yararl  bir  proje  olaca  yorum  tip  rsat  verdi  iniz  ekk  ederim",
                    "yok", "", "", "yok", "ekk", "projeyi  inceliyorum  Umar  katk  bulunurum", "",
                    "Olabilir  tabi  neden  olmasin", "Fikrim  olursa  size  bilgi  veririm", "Yyy", "Yok",
                    "Bende  kazanmak  istiyorum", "", "Destekliyorum", "Yok", "Evet", "Yok", "Yok",
                    "Uyelere  daha  detayl  bilgi  aktarilmali", "Para  kazanmak  istiyorum", "good", "", "Yok", "",
                    "Yok",
                    "Twitter  platformu  zerinden  sosyal  medya  mas  verilmeli  Kripto  piyasas  oradan  yor  neredeyse",
                    "Evet", "Fikrim  yok", "Yoktur", "uan  akl  gelen  bir  yok  ama  gelirse  size  ula", "",
                    "imdilik  yok",
                    "Tfb  projesi  zel  proje  zel  yeniliklerle  hem  tfb  hemde  kullan  lar  kazanacakt  adresinden  bana  ula  abilirsiniz  uygulama  geli  tirme  konusunda  breefing  yapabiliriz",
                    "Ilerleyen  zamanlarda", "", "Fikirlerim  oldugunda  bildirecegin", "Yok",
                    "Tutacak  bir  projeye  benziyor  fakat  yeterli  walpapper  bilgileri  yok  ven  verme  ndan  biraz  olabilir",
                    "Binance  ile  birli  eklinde  rsa  daha  iye  ula  laca  yorum", "Hay",
                    "Prjoenizin  daha  iyi  yerlere  gelmesi  bizide  mutlu  edecektir  sadece  biraz  daha  reklam  verebilirsiziniz  yat  lar  cezbedecek  projelerle  reklamlarla  gelebilirisiniz  Elbette  prjoleriniz  lam  ilerde  sizin  ekibinizin  daha  ileri  gidece  inden  phem  yok  yorumumu  okudysan  ekk  ederim",
                    "iyi", "cok  hostur", "Yok", "Instagram", "Evet", "Guzel", "Yok", "Yok", "", "ekk  ediyorum",
                    "Her  iyi  olmal", "Ahmettkayaa", "Tak  fayda  saglamak  para  kazanmak  istiyorum", "Tfb",
                    "zel  bir  uygulama", "", "daha  arkada  lara  ula  anketleri  artt  rmak  tmak  gerekir",
                    "Evet", "Cok  zel  bir  proje  tebrik  ediyorum", "Konu  daha  yabanc  zamanla", "", "rmkvci",
                    "Yok", "zel", "dont  have  any  idea  yet", "", "imdilik  yok", "Yok", "", "Henuz  degil",
                    "Yok", "Faydal  olacagini  yorum", "", "Yok", "zel  proje", "Yararl  bir  uygulama", "Yok",
                    "Tfb  projesinde  faydali  olabilecegini  yorum", "ekim  limiti  fazla  bence", "ekk  rler",
                    "Bilmiyorum", "", "Hayir", "Abcde", "", "Yoluyla  veya  davet  yontemiyle  tfb  kazinabilir",
                    "Add", "iyisini  siz  bilirsiniz", "uan  yok", "", "Uygulamay  buluyorum",
                    "uygulamayi  yeni  gordum  biraz  bakip  dogruluk  payina  inabdigim  zaman  ort  video  basi  izlenmesi  olan  Youtube  sayfamda  paylasacagim",
                    "", "", "", "nstagram  furkan  celem",
                    "tfb  hakk  nda  detayl  geni  bilgiler  edindik  projenin  ula  mas  elimden  geleni  yapaca",
                    "Yan  yok", "Brx", "", "Yok", "merw", "zel  Bir  bulu", "",
                    "Hen  bir  fikrim  yok  ama  tak  katk  bulunma  fikrini  destekliyorum",
                    "nsanlara  kuracaklar  projerler  hakk  nda  isim  nerisini  bir  taraf  ndan  oylanarak  ans  verebilirsiniz  ben  bir  irket  kurmak  istiyorum  irketim  akl  mda  tane  isim  var  ben  isimleri  sizin  programinz  sayesinde  milyon  inin  fikrini  alarak  meme  yard  olman  Buradan  hizmeti  almak  sizin  tokeninizi  almam  gerekebilir",
                    "Projenin  kripto  piyasas  nda  bulunan  lara  daha  tan  lmas  gerekti  yeni  guncellemeler  ile  ismini  plana  karmas  gerekti  ini  dusunuyorum",
                    "pimapencik  twitter  adresi", "haven  any  idea", "Daha  fazla  reklam", "yok", "",
                    "yeniyim  daha  sonra  fikir  beyan  etmek  isterim  tabiki", "Yok",
                    "Binance  borsas  giri  yapmal", "",
                    "bir  renciyim  uygulama  ile  hem  token  kazan  hem  borsa  hakk  nda  bilgiler  renmek  uma  gidiyor  bir  olarak  destekliyorum",
                    "proje  evesinde  insanlar  lda  finansal  teknolojik  kullan  ile  kazan  layaca",
                    "lar  dilerim", "",
                    "Tfb  gelece  paras  olaca  zel  bir  yat  yapt  Yap  lacak  ncellemeler  ile  daha  iyi  yerleri  hakediyorsunuz  Daha  fazla  etkinlik  oyun  altyap  yla  daha  iyi  noktalara  gelebilece  ini  yorum",
                    "", "", "", "Yeni  bilgiler  nas  yard  olabiliriz  bilmiyorum", "Yok", "Yok",
                    "dapp  projelerine  vetilebilir  Ayr  tutulan  miktar  kadar  mining  kismi  bulunabilir", "",
                    "", "Proje  zel", "zel  bir  uygulama  umutla  bak  yorum", "Yeni  lad", "kemmel  anketcilik",
                    "Destek  ekibinin  bir  par  olarak  projenin  geli  mesine  katk  layabilirim  Sosyal  medya  ara  lar  alanlarda  projenin  bilinirli  ini  art  racak  malar  tebilirim  ile  ileti  ime",
                    "bende  kazanmak  istiyorum", "", "", "Uygulama  aray  daha  iyi  hale  getirebilirsiniz", "",
                    "Ben  lad  kripto  sat  yapmaya  uanl  pek  gelmedi  gelirse  ula  maya", "", "", "", "",
                    "Daha  anla  olmasi", "", "Tfb  projesini  veniyorum",
                    "Proje  ger  ekten  uma  gitti  projenin  niversitelerde  ksek  lisans  tezlerinde  anket  yapmak  isteyen  projesiyle  ilgili  genel  leri  almak  isteyen  iler  faydal  olabilece  ini  yorum  konuda  katk  bulunabilirim  ekk  rler  adresim",
                    "sin", "Yard  mla  arak  kazanmak", "",
                    "ben  Oktay  Bay  instagram  hesabim  Oktaybaay  Youtube  Oktay  Bay", "", "Yok",
                    "Destek  ekibinin  bir  par  olarak  projenin  geli  mesine  katk  layabilirim  Sosyal  medya  ara  lar  alanlarda  projenin  bilinirli  ini  art  racak  malar  tebilirim  ile  ileti  ime",
                    "Arkada  lar  nerdi  memnunlar", "uan  bir  fikrim  yok", "kemmel", "Daha  sonra", "Hay  yok",
                    "", "vrus  exe  instagram  hesab  bir  insan", "", "www  twiter  Muzurboy", "Fikrim  yok",
                    "Hen  yok", "", "vlog  yazard  rarak  projeyi  geli  tirebiliriz", "WhatsApp", "buluyorum",
                    "Yan  yok", "Hen  bilgim  yok  amas  nday", "", "Ekibi  buluyorum", "Yok", "Yakinda",
                    "Referans  yapmak  istiyorum", "anda  yok", "Evet", "", "Yok", "Kat  yorum", "https  alperazak",
                    "", "uygulama", "", "uygulamaya  benziyor  hen  bir  fikrim  yok", "", "Yan  nda  TFB", "Yok",
                    "", "Yok", "Ben  lad  kripto  sat  yapmaya  uanl  pek  gelmedi  gelirse  ula  maya", "Yok",
                    "Huseyin  aksitt  instagram", "Yoktur  bir  fikrim",
                    "asl  nda  pek  bir  fikrim  yok  ama  katk  bulunmak  isterim", "", "", "Yok", "Yok", "",
                    "uguraliakyoll", "", "Antalya  lge  organizasyonlar  nda  aktif  rev  alabilirim",
                    "KARAKASAHMETHAS", "zel", "ekk  rler", "yakup  unsal", "", "", "Hay", "",
                    "TFB  ile  yeni  tan  bir  arkada  sayesinde  Umar  iyi  yerlere  gelir", "", "", "",
                    "zel  her", "Daha  fazla  inin  bilgilendirilmesi  laz", "Deneyelim  pek  anlamadim",
                    "Haberler  saya  gelmeli", "", "", "zel  proje  anketler  kullan  yor  ama",
                    "menekseyasmingmail", "", "Ben  kazanmak  istiyorum", "Olumlu  dusunuyorum", "imdilik  yok", "",
                    "Daha  sonra  denemek  istiyorum",
                    "Bence  daha  iyi  firmalarla  birli  yap  labilir  binance  gibi",
                    "beraber  kazanal  istiyorum", "Heyecan  ariyorum", "lider", "Bende  kazanmak  istiyorum", "",
                    "", "", "anketler  artt  lmal", "iyi", "", "projeyle  herkes  kazanacak", "Guzel  uygulama",
                    "Yeni  yukledim  kazandirmaya  calisicam", "", "Cok  gzel",
                    "konuyu  tam  olarak  bilmiyorum  ama  konuda  fikir  retebilece  imi  yorum  pratik  bir  zekam  var  yani  ben  yle  yorum  odakl  nebiliyorum",
                    "",
                    "gibi  bir  faydam  olabilir  bilmiyorum  ama  katk  bulunmak  isterim  elimden  geldi  ince",
                    "", "sanal  para  bir  zaman  sonra  ger  para  olacak",
                    "projeyi  hem  rklerden  olu  mas  hemde  venilir  uzun  vadeli  bir  lam  proje  olarak  borsalarda  ald  allah  iyi  yerlere  gelcek  herkes  kazancak",
                    "Datan  nemli  oldu  neminin  daha  artaca  zdeki  nlerde  yle  bir  projeye  katk  bulunmak  isterim  olarak  zerinden  ula  abilirsiniz",
                    "Siz  inizi  her  zamans  daha  iyisini  bilirsiniz", "Instagram  kivircikaan", "Yok", "", "",
                    "zel  coin", "Avukat", "Yararl  bir  uygulama", "Yok", "Yok", "Fikrim  var", "Yok", "Yok",
                    "lar",
                    "Kripto  para  ekosistemi  erisinde  rkiye  nin  sahibi  olmas  giri  imcilerinin  ahsi  olarak  destek  isi  olmak  projelerine  destek  bulunmak  bizim  bir  revdir  Kripto  para  kullan  olarak  nyada  ralarda  bulunan  rkiye  TFB  markas  daha  fazla  kitleye  ula  mas  reklam  marka  anla  malar  yapmas  marka  erinin  artmas  nemlidir  Sizlerin  minvalde  atman  heyecanla  beklemekteyim",
                    "Yok", "bir  proje  ama  reklam  yapmal", "", "", "Not  yet", "umutoks", "Yok", "Bilmiyorum",
                    "Faruk", "", "", "Basar  buluyorum", "", "zel  bir  uygulama", "Yok", "", "kenankahraman",
                    "revlerimi  yerime  getirece", "binance  borsas  nda  olsun",
                    "Para  kazanmak  burday  Bana  destek  olacaksan  yard  ihtiya  duyarsan  WhatsApp  numaram",
                    "TfB  miktar  biraz  daha  kseltilmeli",
                    "Tfb  projesinin  faydal  olabilece  ini  yorum  bende  kazanmak  istiyorum", "", "Yok",
                    "need  rich", "Mahmutcelik", "", "Yok", "kripto  para  gelece  nyas  piyasaya  vericek", "Yok",
                    "Daha  sonra", "fikrim  yoktur  ilerleyen  zamanlarda  size  ula", "Jajshskakamabdbdm",
                    "zel  uygulama", "", "ekk  rler", "Tfb  olarak  zel  bir  uygulama", "Yok", "",
                    "Belki  daha  sonra",
                    "Epostada  adres  daha  ncede  buraya  kay  vard  ama  Apple  yak  ncellemeyi  zel  olmu  umar  daha  iyi  yerlere  gelirsiniz",
                    "brokerr", "Projeyi  eniyorum  gayet  iyi  bir  ekilde  ilerliyor",
                    "Daha  ileride  iyi  yerlere  gelece  ine  inan  yorum",
                    "rkiye  coini  olarak  cok  daha  yerlese  gelmemiz  laz", "", "", "Airdrop  yapilmali",
                    "bir  fikrim  yok  ama  projenizi  endim", "Yok", "Bilmiyorum", "", "", "Yok", "", "", "", "",
                    "", "zel", "imdilik  yok", "Daha  pop  ler", "rkiye  nemli  bir  proje  olaca  yorum",
                    "Faydal  buluyorum", "Gayet  zel",
                    "TFB  piyasas  yak  ndan  takip  ediyorum  olduk  buluyorum  fakat  pek  dikkat  ekmeyen  ama  geli  tirilmeye  eksiklikler  var  konuda  farkl  malar  ile  sizleri  desteklemek  yeni  inavasyonlar  katmak  isterim",
                    "", "Babmmac", "", "", "", "Yok", "Bence  twitter  daha  aktif  kullanmal",
                    "lar  devam  diliyorum  hocam  Tan  yoruz  zaten", "",
                    "TFB  nin  daha  aktif  olmas  istiyorum", "bahiskollik", "kazanmak  istiyorum",
                    "krypto  learner  and  media  research  digital  and  marcomms  expert", "", "", "",
                    "Projenin  faydal  olaca  inan  yorum", "Evet", "Jajshsh", "", "", "", "Yok", "Yok",
                    "Merhaba  toplulu  bir  yesi  olmak  isterim  Projenizi  inceledim  olaca  yorum  Tebrikler",
                    "Yok", "Bilmiyorum", "ismailuludag", "herhangi  fikrim  yok", "guzel", "istwmiuorum",
                    "Malesef  bir  fikrim  yok", "", "Heidheie  dheieevue  rueeoehd  eurjdjehej  ejejeheje",
                    "evet  dusunuyorum", "Bende  kazanmak  istiyorum", "",
                    "suleorman  uygulamay  dan  rendim  ahsen  bir  uygulamay  dan  renip  indiriyorum  fakat  uygulama  yor  Fakat  uygulaman  zel  oldu  una  inanarak  uygulamayi  kullanmaya  yorum",
                    "Yok", "Ksjdj", "Yoo", "Facebook", "Yok", "lerde  olaca  inan  yorum",
                    "borsalardaki  satislar  reclamation  nunden  cok  basarili", "Twitter",
                    "uan  bilgim  onerimyok", "Cok  zel  bir  proje  fakat  biraz  pahal  deme  alma  Ama  kemmel",
                    "", "Yok", "WhatsApp",
                    "anlad  kadar  yla  birilerini  projeye  ekmek  verilen  ller  yetersiz  Buradan  tfb  kazan  realize  etmek  zor  yor  Bunun  zeltilmesi  gerekti  ini  yorum",
                    "Ayn  zamanda  projenine  venim  tam  yat  mon  bir  size  yat  kendi  koydu  uzun  vade  olman  gereken  yere  gelmeniz  gelmemiz  heyevanla  takipteyim",
                    "Bilmiyom  yeni  kullaniciyim  gorecez", "pimapencik  twitter  adresi", "", "Kat  yorum",
                    "buluyorum", "", "gizem  yalcinymm", "", "uan  yok", "Yakinda", "www  twiter  Muzurboy",
                    "cevaplamak  istemiyorum", "zel  Bir  bulu", "merw", "Add",
                    "Tfb  projesini  hen  yeni  takibe  yorum",
                    "Yoluyla  veya  davet  yontemiyle  tfb  kazinabilir", "lar  dilerim", "Evet",
                    "proje  evesinde  insanlar  lda  finansal  teknolojik  kullan  ile  kazan  layaca",
                    "Daha  fazla  reklam", "zel", "Bilmem", "kemmel",
                    "farkl  fikirlerim  yok  sekt  hakk  nda  bilgili  ilim  ama  uygulamaya  net  olan  bir  rehber  ekleyebilirsiniz",
                    "", "", "Antalya  lge  organizasyonlar  nda  aktif  rev  alabilirim", "",
                    "Kazanmak  icin  elimden  geleni  yaparim", "", "",
                    "yeniyim  daha  sonra  fikir  beyan  etmek  isterim  tabiki", "Binance  borsas  giri  yapmal",
                    "", "", "", "TFB  ile  yeni  tan  bir  arkada  sayesinde  Umar  iyi  yerlere  gelir",
                    "iyisini  siz  bilirsiniz", "",
                    "Tfb  hakkinda  detayl  bir  bilgiye  sahip  ilim  ama  renince  yay  lmas  katk  sunaca  Kendim  yat  yaparak  geli  mesini  beklemekteyim",
                    "nstagram  furkan  celem", "fikrim  yok", "Gelecek  yorum", "Yok",
                    "arkada  tavsiyesi  zerine  geldim  Faydal  bir  uygulama  olaca  yorum", "Yok",
                    "Hen  bir  fikrim  yok  ama  tak  katk  bulunma  fikrini  destekliyorum",
                    "kripto  paralara  ilgim  var", "KARAKASAHMETHAS", "zel",
                    "Bende  kazanmak  istiyorum  silerim  sayesinde", "",
                    "Daha  yeni  kullanmaya  lad  hen  fikrim  yok", "", "", "Evet  faydal  olarak  dusunuyorum",
                    "", "", "Hay", "zel", "Ekibi  buluyorum", "https  alperazak", "", "", "",
                    "umar  itimime  katk  layacak  kazan  elde  ederim", "", "haven  any  idea", "", "", "Yok",
                    "Umar  projesi  olan  proje  daha  iyi  yerlere  gelir", "Daha  sonra", "Serhatdemiralp",
                    "Projenin  kripto  piyasas  nda  bulunan  lara  daha  tan  lmas  gerekti  yeni  guncellemeler  ile  ismini  plana  karmas  gerekti  ini  dusunuyorum",
                    "Yuu", "sin", "zel", "Yok", "", "Vatsap",
                    "uygulamayi  yeni  gordum  biraz  bakip  dogruluk  payina  inabdigim  zaman  ort  video  basi  izlenmesi  olan  Youtube  sayfamda  paylasacagim",
                    "Hay  yok", "zel  her", "anda  yok", "", "Yok", "Bilgim  yok", "", "Hen  yok", "",
                    "uguraliakyoll", "zel  proje", "Bile  yok", "",
                    "TGB  projesi  hakk  nda  hen  fazla  bilgim  yok  deneyimlerimi  arkada  lar  ile  payla  kat  lmalar  lar",
                    "fazla  tfb  uygulamas  yayarak  geni  kitlelere  ula  mak", "", "Yok",
                    "Sosyal  platformlarda  reklam", "Yoktur", "sadece  yat  olarak  yer  almak  istiyorum",
                    "vlog  yazard  rarak  projeyi  geli  tirebiliriz", "",
                    "uygulamaya  benziyor  hen  bir  fikrim  yok", "ekk  rler", "Yok",
                    "mailimden  ban  ula  abilirsiniz  uygulaman  yararl  oldu  unu  yorum", "", "esmekat",
                    "whatsapp", "", "evet", "Arkada  lar  nerdi  memnunlar", "", "", "zel", "", "",
                    "Hen  bilgim  yok  amas  nday", "", "Tuncay  Eren  Albayrak", "", "yakup  unsal", "Yok", "",
                    "Kazanmak  istiyorum", "Yok", "Yoktur  bir  fikrim", "Yard  mla  arak  kazanmak", "",
                    "Daha  fazla  yat  bulmam  gerekebilir",
                    "EmuSSaMe  Kripto  para  piyasas  belli  bir  seviye  bilen  farkl  projeleri  incelemi  birisiyim  Geli  tirmek  farkl  fikirlerin  olabilir",
                    "Yok", "Yok", "", "nce  bir  ara  rma  yapay  size  ncelerimi  iletirim", "", "yok", "", "",
                    "Eme  inize", "Ger  ekten  ileriye  harika  bir  proje  olmu  ellerinize",
                    "Huseyin  aksitt  instagram", "yorum", "Fikrim  yok",
                    "Proje  ger  ekten  uma  gitti  projenin  niversitelerde  ksek  lisans  tezlerinde  anket  yapmak  isteyen  projesiyle  ilgili  genel  leri  almak  isteyen  iler  faydal  olabilece  ini  yorum  konuda  katk  bulunabilirim  ekk  rler  adresim",
                    "Yok",
                    "nsanlara  kuracaklar  projerler  hakk  nda  isim  nerisini  bir  taraf  ndan  oylanarak  ans  verebilirsiniz  ben  bir  irket  kurmak  istiyorum  irketim  akl  mda  tane  isim  var  ben  isimleri  sizin  programinz  sayesinde  milyon  inin  fikrini  alarak  meme  yard  olman  Buradan  hizmeti  almak  sizin  tokeninizi  almam  gerekebilir",
                    "asl  nda  pek  bir  fikrim  yok  ama  katk  bulunmak  isterim", "Bilemiyorum", "Yok", "Yok",
                    "Beklemedeyim", "", "Gelecek  vaadediyor",
                    "projenin  geli  mesi  yeni  anla  malarin  yap  lmas  gerekiyor", "Herhangi  bir  mam  olmad",
                    "", "", "Bence  twitter  daha  aktif  kullanmal",
                    "Tfb  hakkinda  detayl  bir  bilgiye  sahip  ilim  ama  renince  yay  lmas  katk  sunaca  Kendim  yat  yaparak  geli  mesini  beklemekteyim",
                    "Bilgim  yok", "zel", "Yok", "Bende  kazanmak  istiyorum  silerim  sayesinde",
                    "kripto  paralara  ilgim  var", "Tfb  projesini  hen  yeni  takibe  yorum",
                    "Daha  yeni  kullanmaya  lad  hen  fikrim  yok", "", "Tfb  projesinin  iyi  oluca  yorum",
                    "Yok", "Uygulama  aray  daha  iyi  hale  getirebilirsiniz", "Hen  sizi  tan  maya  yorum", "",
                    "Ger  ekten  ileriye  harika  bir  proje  olmu  ellerinize", "Tuncay  Eren  Albayrak", "Evet",
                    "lar", "Umar  projesi  olan  proje  daha  iyi  yerlere  gelir", "fikrim  yok",
                    "Binance  gibi  borsalarda  kendinizi  sterebilirseniz  coinin  pop  lerli  eri  artacakt  diye  yorum",
                    "", "", "zel  proje", "", "Projede  faydal  olabile  imi  yorum",
                    "ncelikle  merhaba  ben  kendimi  projeye  yak  hissediyorum  Benimle  ileti  kurarsan  fikirlerimi  sizinle  payla  mak  isterim  iyi  ali  malar  dilerim  telefon  numaras  kullan  hsnyrlmzz",
                    "", "",
                    "EmuSSaMe  Kripto  para  piyasas  belli  bir  seviye  bilen  farkl  projeleri  incelemi  birisiyim  Geli  tirmek  farkl  fikirlerin  olabilir",
                    "", "zel", "mailimden  ban  ula  abilirsiniz  uygulaman  yararl  oldu  unu  yorum", "yorum",
                    "Herhangi  bir  mam  olmad", "", "", "", "",
                    "farkl  fikirlerim  yok  sekt  hakk  nda  bilgili  ilim  ama  uygulamaya  net  olan  bir  rehber  ekleyebilirsiniz",
                    "Kazanmak  istiyorum", "", "fazla  tfb  uygulamas  yayarak  geni  kitlelere  ula  mak", "Yok",
                    "Daha  anla  olmasi", "Binance  listelemesi", "", "Fikrim  yok", "Serhatdemiralp",
                    "Kazanmak  icin  elimden  geleni  yaparim", "Yok", "Bilmem", "", "Yok", "gizem  yalcinymm",
                    "cevaplamak  istemiyorum", "Beklemedeyim", "Yuu", "", "Bile  yok", "",
                    "umar  itimime  katk  layacak  kazan  elde  ederim", "Vatsap", "", "", "", "Eme  inize", "Yok",
                    "", "Sosyal  platformlarda  reklam", "Bilemiyorum", "Bende  burday", "", "whatsapp", "", "Yok",
                    "guzel", "sadece  yat  olarak  yer  almak  istiyorum",
                    "imin  nerisiyle  kullanmak  istiyorum  zel  bir  proje  oldu  unu  yorum",
                    "Binance  gibi  borsalarda  kendinizi  sterebilirseniz  coinin  pop  lerli  eri  artacakt  diye  yorum",
                    "Yan  nda  TFB", "gayet  guzel", "", "Yok", "Fikrim  yok", "Uygulamay  buluyorum",
                    "Tfb  projesinin  iyi  oluca  yorum", "", "Binance  listelemesi", "", "lar", "", "Yok", "Evet",
                    "Arkada", "", "imin  nerisiyle  kullanmak  istiyorum  zel  bir  proje  oldu  unu  yorum", "",
                    "", "", "Referans  yapmak  istiyorum", "iyi", "", "Bende  burday", "Hay  yok",
                    "bir  renciyim  uygulama  ile  hem  token  kazan  hem  borsa  hakk  nda  bilgiler  renmek  uma  gidiyor  bir  olarak  destekliyorum",
                    "", "Daha  fazla  inin  bilgilendirilmesi  laz", "Projede  faydal  olabile  imi  yorum", "Yok",
                    "Tak  katk  bulunarak  bende  kazanmak  istiyorum", "",
                    "tfb  hakk  nda  detayl  geni  bilgiler  edindik  projenin  ula  mas  elimden  geleni  yapaca",
                    "", "Yok",
                    "Simdilik  yeniyim  icerik  konusunda  daha  kapsamli  bir  bilgi  birikim  sdindikce  eksikler  artilar  konusunda  fikir  beyaninda  bulanacagim",
                    "", "dont  have  any  comment  about  this  but  follow", "", "", "evet", "Yok",
                    "Bilmiyom  yeni  kullaniciyim  gorecez", "", "zel", "esmekat",
                    "projenin  geli  mesi  yeni  anla  malarin  yap  lmas  gerekiyor", "Yeni  lad", "gayet  guzel",
                    "TGB  projesi  hakk  nda  hen  fazla  bilgim  yok  deneyimlerimi  arkada  lar  ile  payla  kat  lmalar  lar",
                    "Daha  fazla  yat  bulmam  gerekebilir", "nce  bir  ara  rma  yapay  size  ncelerimi  iletirim",
                    "Yoktur", "ekk  rler", "Yok", "Evet  faydal  olarak  dusunuyorum", "Yok", "", "",
                    "Herhangi  bir  fikrim  yok", "", "WhatsApp", "", "", "", "Yok", "Yok",
                    "Tfb  olarak  zel  bir  uygulama", "Hay  yok",
                    "Tak  katk  bulunarak  bende  kazanmak  istiyorum", "", "zel", "",
                    "Kriptoda  yeni  oldu  umdan  bir  fikir  retemeyece",
                    "arkada  tavsiyesi  zerine  geldim  Faydal  bir  uygulama  olaca  yorum", "Yok", "imdilik  yok",
                    "Simdilik  yeniyim  icerik  konusunda  daha  kapsamli  bir  bilgi  birikim  sdindikce  eksikler  artilar  konusunda  fikir  beyaninda  bulanacagim",
                    "Yok", "uygulama", "Meil", "WhatsApp", "Yok", "Siverek", "Hakan", "Recep  adresim", "",
                    "Ankete  kat  lan  inin  sorulabilir", "Yok",
                    "Projeye  kat  lmak  ama  daha  fazla  yenilik  oyun  geli  tirme  rekklam  art  yap  labilir",
                    "zerine  hen  nmedim  ama  dikkatle  inceleyecd", "zel  uygulama", "Hay", "Aaaa", "Kazan",
                    "Ogrenecez", "Yok", "", "Daha  fazla  anket  olmas  daha  iyi  olur", "Thank  you",
                    "Fikrim  yok", "", "https  theGreatOzzy", "yorum  her  iyi  olacak", "Kullan  kolayl",
                    "evremin  zel  sosyal  hayat  geni  oldu  unu  yorum  sebepten  size  reklam  ndan  faydal  olabilece  imi  yorum  adresim",
                    "TFB  projesini  twitter  arac  yla  olduk  venilir  bir  iden  duydum  ayni  zamanda  bir  tfb  yatirimcisiyim  elimden  gelen  bir  sey  olmasi  durumunda  yard  olmak  isterim  karsilikli  bir  winwin  durumu  proje  hakkinda  detayl  bir  bilgi  almak  isterim  bunun  icin  adresim  projeyi  daha  detayl  arastirip  bilgi  alisverisi  yapabiliriz",
                    "", "yok", "Whatsup", "", "Daha  iyi  olaca  inaniyirum", "Evet", "Uygulamay  daha  fediyorum",
                    "imdilik  bir  fikir  yok", "", "Evet", "Facebook", "Yok  maalesef",
                    "Bence  iyi  gidiyor  zel  miktarlar  kazan  labilir", "Pasif  gelir", "Bilemiyomki", "Yok",
                    "Yok",
                    "global  lkelerin  dil  deste  veri  yerine  yeni  globalde  yeni  nler  gelmesi  global  borsalarda  listelenme  tabiki  reklam  NFT  uygulaman  reklam  firmalar  analiz  firmalar  ile  anla  mas  anketlerin  revlerin  alt  lmas  tfb  ekim  limitinin  kolayla  mas",
                    "insan  yat  yaparken  elinde  olmayan  bir  eye  yat  yaparken  korkar  heyecan  Abartmayi  dedikoduyu  sever  sebepten  dolay  bedava  dan  coin  kazanarak  hesaplar  nda  kar  rse  patlama  yapar  reklam  alas  olur",
                    "Tamam", "", "lar", "", "Tfb  gelece",
                    "Proje  reklamlar  iyi  olsun  fazlas  yla  yeterli  olacakt", "Mithat  bali",
                    "Birlik  ven  ercevesi  inde  Olursak  Herkes  Kazan",
                    "uygulamay  kullan  uygulaman  daha  geni  kitlelere  yay  lmas  istiyorum",
                    "detayl  incelemedim  belki  ileride", "Kaybetmeden  kazanamazsiniz", "Maalesef  yok",
                    "zel  proje", "Faydal  olaca  yorum  arkas  nday  projenin  zel  bir  proje  olmu",
                    "Yakla  bir  seneden  beri  stake  coinlerine  yat  yap  yorum  mpax  dxc  talenT  retip  sat  yorum  teknik  analiz  konusunda  itim  yorum  ayr  hukuk  fak  ltesinde  itim  yorum  adresinden  benimle  ileti  ime  ebilirsiniz",
                    "Tak  katk  bulunarak  bende  kazanmak  istiyorum", "", "uan  fikrim  yok",
                    "Whatsap  gruplar  labilir", "", "", "Yok", "", "buluyorum", "", "Istagram", "arzusevincaslan",
                    "", "Suan  icin  yok", "", "Kkaxx", "Bilmiyorum", "yorum", "zel  bir  proje", "fikrim  yok", "",
                    "", "Bilgi  vermek  istemiyorum", "",
                    "Verilen  kazan  lar  bir  tik  daha  kselmesi  insanlar  daha  cazip  bulup  daha  iye  ula  mas",
                    "youtubede  videolar  izliyorum  bir  projenizi  destekliyor  umar  hak  etti  iniz  yerlere  ula",
                    "ekk", "hedefe  varmak", "", "Farkl  oyunlar  eklenebilir", "",
                    "adresimden  ulasilabilir  gelece  yat  arac  olarak  mecrada  takimimla  birlikte  daha  ksek  gelir  elde  etmek",
                    "farkl  oyunlar  eklenebilir", "Kripto  para  sat  yorum", "", "Yok", "uan  bir  fikrim  yok",
                    "ben  arkada  taraf  ndan  buldum  corona  neminde  bana  kazan  lica  yorum", "yok",
                    "Kendine  ait  bir  staking  veya  hodl  sisteminin  projeye  cok  katki  sagalayacgini  dusunuyorum  bir  doktor  olarak  saglik  calisanlarina  bonus  getirilerinin  reklam  acisindan  mantikli  olcagini  dusunuyorum",
                    "Hay", "ekk  rler", "", "Yok", "Yoktur", "Tabikide  istiyorum  instagram", "yok", "Yok", "",
                    "Evt",
                    "proje  hakk  nda  pek  bir  soyleyemeyecegim  pek  bilmiyorum  arkada  dedi  yle  var  indir  yap  bende  yap  yorum  kusura  bakmay  ilerleyen  tarihlerde  bir  fikir  alg  olu  ursa  kafamda  bunu  sizinle  payla  mak  isterim",
                    "renciyim  geni  bir  evreye  sahibim  payla  mlarla  etkileyebilirim", "zveriliyim",
                    "Hay  malesef  yok", "Yok", "Sonra", "tfb  projesini  buluyorum  arkada  lar  tavsiye  edece",
                    "", "Ercan", "", "", "Umar  olursunuz", "", "nope", "telefon  numaram  ise",
                    "Kriptoda  yeni  oldu  umdan  bir  fikir  retemeyece", "Daha  iyi  yerlere  gelecek", "", "",
                    "", "ekim  oran  lmeli", "", "kendime  veniyorum  tak  katk  bulunmak  burday",
                    "projeyi  buluyorum  projeler  inde  tfbnin  iyisi  olaca  yorum", "Yok",
                    "her  eyde  nce  Projesi  olu  iden  iye  llendirme  sistemini  enerek  destekliyorum  bir  inin  lenceli  zevkli  olu  umu  destekleyece  ine  inanc  tam  Hem  oyna  hem  kazan",
                    "", "proje", "Yok", "resitalex", "zel  uygulama", "Yok", "",
                    "Kendim  proje  reten  birisi  olarak  projelerin  faydal  olabilece  ini  yorum", "Tamam",
                    "Zbzbznnz", "Yok", "Yok", "", "zel  kazan", "Bfjfnfdj", "",
                    "Daha  iye  yay  lmal  reklam  olabilir",
                    "Tfb  projesi  hakk  nda  internette  yeterli  klay  bilgi  bulunmad  yorum  Twitter  bile  aratt  mda  bilgilere  ula  yor  oda  bir  inin  payla  tfb  art  sterdi  zaman  zaten  ndem  olacakt  ama  umar  yak  zamanda  olur",
                    "Emal  Talha  Yalgin", "", "Bilgim  olan  bir  piyasa", "projenin  zel  olaca  inan  yorum", "",
                    "", "", "Guzel  hayirlisi", "", "Hhh", "Mant  bir  projesin  sana  ylenecek  laf  yok",
                    "Evet  faydal", "Yok", "Bende  projenin  parcasi  olacagin", "Belli  olmadi", "", "",
                    "Bil  kazan", "", "Asd", "Yok",
                    "Yeni  lam  proje  oldu  unu  duydum  ula  mas  elimden  geleni  yapar", "Yok", "Ghcxz",
                    "Yok  malesef", "Bence  harikas  aynen  yle  devam", "", "lerde  olabilir",
                    "Tfb  uygulamas  gelece  ini  parlak  yorum", "Maalesef  akl  bir  gelmiyor", "Evet", "",
                    "Uygulamay  daha  zel  sorunsuz  yapabilirsiniz", "", "Oyun  say  art  labilir",
                    "Deneyip  rece", "imdilik  yok",
                    "ncelikle  merhaba  ben  kendimi  projeye  yak  hissediyorum  Benimle  ileti  kurarsan  fikirlerimi  sizinle  payla  mak  isterim  iyi  ali  malar  dilerim  telefon  numaras  kullan  hsnyrlmzz",
                    "", "uan  bir  fikrim  yok", "", "Hen  sizi  tan  maya  yorum", "Yok",
                    "ben  Oktay  Bay  instagram  hesabim  Oktaybaay  Youtube  Oktay  Bay", "",
                    "dont  have  any  comment  about  this  but  follow", "vrus  exe  instagram  hesab  bir  insan",
                    "", "allah  zel  ler  olur", "Yusufdemiroutlook", "Not  now",
                    "Para  kazanmak  girdim  alah  kazan", "", "", "", "ekk", "allah  herkes  kazanacak", "Belki",
                    "fikrim  yok", "Yok", "zel", "", "", "", "Yeni  oyunlar  gelmeli", "", "",
                    "https  www  facebook  nazmi  sosyal  medya  ortam  nda  irdi  uzun  zaman  kendime  faydas  olacak  ekilde  kullanmak  isterim",
                    "Yenilikci  spesifik  her  eye  acigimdir  Ayr  hukuki  konularda  kendime  guvdniyorum  Twitter  burakgunulu",
                    "Yok", "Hay", "", "Fikrim  yok  sadece  yatirimciyim", "Yok",
                    "Ilerde  bilgi  sahibi  olursam  bilgi  veririm  artik", "",
                    "nternetten  veri  zaten  yap  yoruz  Pop  ler  siteler  yada  bilinenler  TFB  ile  yaparsak  TFB  alal",
                    "zel  proje", "Maalesef  yok", "", "Kazanmak  istiyorum  umar  kazan", "",
                    "yararl  bir  proje  ger  ekten", "instagram  nercly", "Hayir", "", "Binance  listelenmeli",
                    "uan  yok", "Binance  listelenmeli", "", "Dilek  Ataker", "Basarili", "", "uanda  inceliyorum",
                    "Fikrim  yok  sadece  yat", "", "Yok", "Yok", "", "bir  uygulama", "", "",
                    "Kullan  amac  geli  tirilebilir", "hen  bilmiyorum  rece", "Umar  iyi  yerlere  gelirsiniz",
                    "iyi", "", "ideas  yet", "", "", "", "", "Maalesef",
                    "freelancer  student  artist  think  you  can  for  logo  update  feel  like  logo  needs  new  more  crypto  currency  based  vibe",
                    "", "Para  kazanmak", "",
                    "renciyim  tfb  projesinin  gelece  inin  parlak  oldu  unu  yorum  ayd  giden  yolda  bende  katk  bulunmak  istiyorum",
                    "zel", "iyi", "Yok", "Yok", "Para",
                    "Sadece  duydum  geldim  zaman  sterecek  bilmiyorum  uygulamaya  hakk  nda  bilgim  bile  yok  biraz  zaman  gerekli",
                    "",
                    "Tarih  soru  haz  rlanmas  nda  diger  konularda  faydal  olacag  yorum  tarih  konusunda  konusunda  bilgim  cok",
                    "Evet", "", "", "Hay  yok  olursa  yazar", "", "new  will  thinking  about", "Yok",
                    "fikrim  bulunmamakta", "", "stemiyorum", "ula  rsan  bilgilendiririm", "", "Yolunuz  olsun",
                    "", "Yok",
                    "Trb  projesinde  faydal  olabilece  imi  yorum  tak  katk  bulunarak  bende  kazanmak  istiyorum",
                    "Bol  Reklam  bol  yatirim", "eklendirme  yapmal", "", "lknurdemirsaha  arvenilac", "",
                ],
            },
        };
    }
    plotInterface = buildViz(1000, 600, null, null, false, false, false, false, false, true, false, false, true, 0.1,
        false, "Log Frequency", "Rosengren's S", getDataAndInfo(), false, false,
        function (d) {
            return (d.term + "<br />Log Frequency: " + d.etc["Xpos"].toFixed(6) + "<br />Rosengren&#x27;s S: " + d
                .etc["Ypos"].toFixed(6));
        }, null, null,
        function (d) {
            return d3.interpolateRdYlBu(d.etc["ColorScore"]);
        }, true, false, true, false, null,
        ["More Dispersion", "Medium", "Less Dispersion"], 10, null, null, null, true, true, true, undefined, null,
        false, false, ".3f", ".3f", false, -1, true, false, true, false, false, true, true,
        (d) => "Term: " + d.term + "<div class=topic_preview>" + "<b>Frequency:</b> " + d.etc["Frequency"] +
        "<br />" + "<b>Range:</b> " + d.etc["Range"] + "<br />" + "<b>SD:</b> " + d.etc["SD"].toFixed(6) +
        "<br />" + "<b>VC:</b> " + d.etc["VC"].toFixed(6) + "<br />" + "<b>Juilland&#x27;s D:</b> " + d.etc[
            "Juilland's D"].toFixed(6) + "<br />" + "<b>Rosengren&#x27;s S:</b> " + d.etc["Rosengren's S"].toFixed(
            6) + "<br />" + "<b>DP:</b> " + d.etc["DP"].toFixed(6) + "<br />" + "<b>DP norm:</b> " + d.etc[
            "DP norm"].toFixed(6) + "<br />" + "<b>KL-divergence:</b> " + d.etc["KL-divergence"].toFixed(6) +
        "<br />" + "<b>DA:</b> " + d.etc["DA"].toFixed(6) + "<br />" + "<b>Expected:</b> " + d.etc["Expected"]
        .toFixed(6) + "<br />" + "<b>Residual:</b> " + d.etc["Residual"].toFixed(6) + "<br />" +
        "<b>ColorScore:</b> " + d.etc["ColorScore"].toFixed(6) + "<br />" + "</div>", {
            upper: "Lower than Expected",
            lower: "More than Expected",
        }, {
            lower: (a, b) => a.etc["Residual"] - b.etc["Residual"],
            upper: (a, b) => b.etc["Residual"] - a.etc["Residual"],
        }, true, null, undefined, undefined, undefined, "#e5e5e3", undefined, undefined, undefined);
    autocomplete(document.getElementById("searchInput"), plotInterface.data.map((x) => x.term).sort(), plotInterface);
</script>
    '''),
    ])

# import dash_t

# def year_maker(row):
#     now_year=int(str(datetime.datetime.now())[:4])
#     if row['Дата нач. экспл.']==0:
#         return 'Утеряна летопись'
#     elif now_year- int( str(row['Дата нач. экспл.'])[-4:])<=3:
#         return 'до 3 лет'
#     elif now_year- int( str(row['Дата нач. экспл.'])[-4:])<=5:
#         return 'до 5 лет'
#     elif now_year- int( str(row['Дата нач. экспл.'])[-4:])<=7:
#         return 'до 7 лет'
#     elif now_year- int( str(row['Дата нач. экспл.'])[-4:])>7:
#         return 'более 7 лет'

# @cache.memoize()
# def it_get_df(date):

#     df=pd.read_excel('it.xls',encoding='utf-8')
#     #меняем пустые строки на 0
#     df=df.fillna(0)
#     return df


# def layout():


#     load_time=str(datetime.datetime.now())
#     load_time=load_time[:15]

#     main_df=it_get_df(load_time)

#     departments=main_df[main_df['РабочееМесто']!=0]['РабочееМесто'].unique().tolist()
#     departments.append('Все')
#     return html.Div([

#     html.Div([html.H3('IT devices' )],style={'text-align':'center'}),
#     html.Div(id='stored_data',children=load_time,style={'display':'none'}),

#     html.Div([
#          html.Div([dcc.Dropdown(id='department',options=[{'label' : i, 'value' : i } for i in departments],value='Все')],style={'width':'100%','display':'inline-block','text-align':'center'})

#     ]),

#     html.Div([dcc.Graph(id='main_view')
#                         ], style={'width': '100%', 'display': 'inline-block'}),

#     html.Div([dcc.Graph(id='age')],style={'width': '49%', 'display': 'inline-block'}),
#     html.Div([html.H4(id='table_info'),dt.DataTable(rows=[{}],
#         # optional - sets the order of columns
#         columns=['Наименование','Количество'],
#         row_selectable=False,
#         #filterable=True,
#         sortable=True,
#         editable=False,
#         id='device_info'
#         )],style={'width': '49%', 'display': 'inline-block'})
#     ])


# @app.callback(
# dash.dependencies.Output('main_view','figure'),
# [dash.dependencies.Input('stored_data','children')
# ,dash.dependencies.Input('department','value')
# ])

# def update_main_view(stored_data,department):

#     main_df=it_get_df(stored_data)

#     if department!='Все':
#         main_df=main_df[main_df['РабочееМесто']==department]


#     main_df=main_df[['Вид оборудования', 'Фирма', 'РабочееМесто']].groupby(['Вид оборудования']).agg({'Фирма': len, 'РабочееМесто': lambda x: len(x[x!=0])})
#     main_df=pd.DataFrame(main_df.to_records())

#     return {
#                         'data':[
#                         {'x': main_df['Вид оборудования'], 'y': main_df['Фирма'] ,'marker':{'color':'#d0cbd8'}, 'type' : 'bar'  , 'name' : 'Всего оборудования'}
#                         ,{'x': main_df['Вид оборудования'], 'y': main_df['РабочееМесто'] ,'marker':{'color':'#41a270'}, 'type' : 'bar' , 'name' : 'В эксплуатации'}
#                         ],
#                         'layout':{ 'hovermode' : 'closest',"font": {"size": 10}}
#                         }

# @app.callback(
# dash.dependencies.Output('age','figure'),
# [dash.dependencies.Input('stored_data','children')
# ,dash.dependencies.Input('department','value')
# ,dash.dependencies.Input('main_view','clickData')
# ])


# def update_age_graph(stored_data,department,device_type):


#     main_df=it_get_df(stored_data)

#     if department!='Все':
#         main_df=main_df[main_df['РабочееМесто']==department]

#     #Фильтруем по типу оборудования
#     try:
#         device=device_type['points'][0]['x']
#     except TypeError:
#         device='ПК'

#     main_df=main_df[main_df['Вид оборудования']==device]

#     #добавим новую колонку с годом ввода в эксплуатацию
#     main_df['год'] = main_df.apply (lambda row: year_maker (row),axis=1)

#     main_df=main_df[['год', 'РабочееМесто']].groupby(['год']).agg({'РабочееМесто': lambda x: len(x[x!=0])})
#     main_df=pd.DataFrame(main_df.to_records())
#     title_text=device + ' в эксплуатации'
#     return {
#     'data':[go.Pie(labels=main_df['год'],values=main_df['РабочееМесто']
#                         ,hoverinfo='label+value+percent'
#                         ,textinfo='percent'
#                         ,marker={'colors':['rgba(65, 162, 112,0.9)','rgba(65, 162, 112,0.7)','rgba(65, 162, 112,0.5)','rgba(65, 162, 112,0.3)','rgba(65, 162, 112,0.1)']}
#                         )]
#     ,'layout':{'title': title_text}
#     }


# @app.callback(
# dash.dependencies.Output('device_info','rows'),
# [dash.dependencies.Input('stored_data','children')
# ,dash.dependencies.Input('department','value')
# ,dash.dependencies.Input('main_view','clickData')
# ,dash.dependencies.Input('age','clickData')
# ])

# def update_device_info(stored_data,department,device_type,age):

#     main_df=it_get_df(stored_data)

#     #Убираем те что не в эксплуатации
#     main_df=main_df[main_df['РабочееМесто']!=0]

#     if department!='Все':
#         main_df=main_df[main_df['РабочееМесто']==department]


#     #Фильтруем по типу оборудования
#     try:
#         device=device_type['points'][0]['x']
#     except TypeError:
#         device='ПК'

#     main_df=main_df[main_df['Вид оборудования']==device]

#     #добавим новую колонку с годом ввода в эксплуатацию
#     main_df['год'] = main_df.apply (lambda row: year_maker (row),axis=1)

#     #Фильтруем по годам в эксплуатации
#     try:
#         years_old=age['points'][0]['label']
#     except TypeError:
#         years_old='до 3 лет'

#     main_df=main_df[main_df['год']==years_old]

#     main_df=main_df[['Наименование', 'РабочееМесто']].groupby(['Наименование']).agg({'РабочееМесто': lambda x: len(x[x!=0])})
#     main_df=pd.DataFrame(main_df.to_records())
#     main_df.columns=['Наименование','Количество']

#     return main_df.to_dict('records')


# @app.callback(
# dash.dependencies.Output('table_info','children'),
# [dash.dependencies.Input('department','value')
# ,dash.dependencies.Input('main_view','clickData')
# ,dash.dependencies.Input('age','clickData')
# ])

# def update_table_indo(department,device_type,age):

#     label=department + ' СО '

#     try:
#         device=device_type['points'][0]['x']
#     except TypeError:
#         device='ПК'

#     label=label + device + ' '

#     try:
#         years_old=age['points'][0]['label']
#     except TypeError:
#         years_old='до 3 лет'

#     label=label + years_old + ' в эксплуатации'

#     return label
