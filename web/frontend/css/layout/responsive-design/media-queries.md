## Media Queries
    Media queries are used to apply CSS, only when environment matches defined rules. It can also be used to detect details about the environment.

    Simplex syntax looks like below:

    @media media-type and (media-feature-rule) {
        Some CSS
    }

    media-type tells browser what kind of media this code for such as print, screen, etc. Default is all.
    media-feature-rule is a rule that must be passed in order to apply CSS in the body. Generally, viewport width is detected to apply CSS by using
features such as max-width, min-width, min.

    Make body color red if view port width equals to 600px.
    @media screen and (width: 600px) {
        body {
            color: red;
        }
    }

    Complex media queries can be constructed by using and/or logical operators:

    @media screen and (width: 600px) and (orientation: landscape)

    To test if one query is matched or another:
    @media screen and (min-width: 600px), screen and (orientation: landscape)