module.exports = {
  "env": {
    "browser": true,
    "es6": true,
    "node": true
  },
  "parser": "babel-eslint",
  "extends": [
    "airbnb",
    "prettier",
    "prettier/babel",
    "prettier/standard"
  ],
  "globals": {
    "Atomics": "readonly",
    "SharedArrayBuffer": "readonly"
  },
  "parserOptions": {
    "ecmaFeatures": {
      "jsx": true
    },
    "ecmaVersion": 2018,
    "sourceType": "module"
  },
  "plugins": [
    "babel",
    "react",
    "react-hooks",
    "prettier"
  ],
  "rules": {
    "semi": ["error", "never"],
    "comma-dangle": ["error", "never"],
    "prettier/prettier": "error",
    "no-use-before-define": ["error", {
      "functions": false,
      "classes": true
    }],
    "no-console": "off",
    "no-param-reassign": ["error", {
      "props": false
    }],
    "react-hooks/rules-of-hooks": "error"
  }
};
