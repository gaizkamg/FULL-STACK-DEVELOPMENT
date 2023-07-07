'use strict';

let moment = require('moment');

/**
 * Returns a string element with a footer and updating year
 * @param {string} name
 * @return {String}
 */

exports.footer = function (name){
    return `Copyright ${moment().format('YYYY')}  ${name} All rights reserved`
};

