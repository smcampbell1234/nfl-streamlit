app_css = """
    <style>
        /**********************************************/
        /* BOILER PLATE STYLE --DO NOT TOUCH          */
        /**********************************************/

        /***** HEADERS **********/
        /* equivalent to streamlit markdown: # */
        .h1 {
            font-size: 2.60rem;
            font-family: "Source Sans Pro", sans-serif;
            font-weight: 700;
            # color: rgb(49, 51, 63);
            line-height: 1.2;
            letter-spacing: -0.005em;        
        }
        /* equivalent to streamlit markdown: # */
        .h2 {
            font-size: 2.25rem;
            font-family: "Source Sans Pro", sans-serif;
            font-weight: 600;
            # color: rgb(49, 51, 63);
            line-height: 1.2;
            letter-spacing: -0.005em;        
        }
        /* equivalent to streamlit markdown: # */
        .h3 {
            font-size: 1.75rem;
            font-family: "Source Sans Pro", sans-serif;
            font-weight: 600;
            # color: rgb(49, 51, 63);
            line-height: 1.2;
            letter-spacing: -0.005em;        
        }
        /* equivalent to streamlit markdown: # */
        .h4 {
            font-size: 1.5rem;
            font-family: "Source Sans Pro", sans-serif;
            font-weight: 600;
            # color: rgb(49, 51, 63);
            line-height: 1.2;
            letter-spacing: -0.005em;
         }
         /* equivalent to streamlit markdown: # */
        .h5 {
            font-size: 1.25rem;
            font-family: "Source Sans Pro", sans-serif;
            font-weight: 600;
            # color: rgb(49, 51, 63);
            line-height: 1.2;
            letter-spacing: -0.005em;
         }
         /* equivalent to streamlit markdown: # */
        .h6 {
            font-size: 1rem;
            font-family: "Source Sans Pro", sans-serif;
            font-weight: 600;
            # color: rgb(49, 51, 63);
            line-height: 1.2;
            letter-spacing: -0.005em;
         }

         /**** STREAMLIT SPECIFIC ********/
        .st-font {
            font-family: "Source Sans Pro", sans-serif;
        }

         /**** COLORS ********/
         .light-gray { color: 	#DCDCDC;  }
         .mid-gray { color: #A9A9A9 !important;}
         .gray { color: #808080; }
         .dark-gray { color: #202020 }

         .light-green { color: #4da64d}
         .green { color: green}
         .dark-green { color: #5F8575}

         /**** Use Light-red to match streamlit's checkboxes ****/
         .light-red { color: #fc4c4c}
         .red { color: red}
         .dark-red { color: #880808}
         .tomato { color: tomato }

         .dark-blue { color: navy}
         .blue { color: #1171cd}
         .golden-rod { color: #DAA520}
         .black { color: black;}


         /**** FLEX BOX *********/
         .space-between {
            display: flex;
            justify-content: space-between;
         }
         /**** FORMATING ********/
         .center {
            text-align: center;
         }
        .tiny {
            font-size: .75rem;
        }
        .small {
            font-size; .8rem;
            font-family: "Source Sans Pro", sans-serif;
         }
         .mid {
            font-size: 1.2rem;
            font-family: "Source Sans Pro", sans-serif;
         }
         .big {
            font-size: 1.4rem;
            font-family: "Source Sans Pro", sans-serif;
         }
         .italic {
            font-style: italic;
         }
         .bold {
            font-weight: bold;
         }
         .label_wrapper {
            margin: 10px;
         }
         .easy-margin {
            margin: 10px;
         }
         .easy-top-bottom-margin {
            margin-top: 10px;
            margin-bottom: 10px;
         }
        .game-score-top-bottom-margin {
            margin-top: 16px;
            margin-bottom: 15px;
         }
         .hard-margin {
            margin: 20px;
         }
        .margin-lr-10p {
            margin-left: 10%;
            margin-right: 10%;
         }
        .margin-lr-15p {
            margin-left: 15%;
            margin-right: 15%;
         }
        .margin-lr-20p {
            margin-left: 20%;
            margin-right: 20%;
         }
        .hard-top-bottom-margin {
            margin-top: 15px;
            margin-bottom: 25px;
         }
         .padding-left-20 {
            padding-left: 10px;
         }
         .margin-top-45 {
            margin-top: 45px;
         }
         .margin-bottom-25 {
            margin-bottom: 25px;
         }
        .margin-bottom-15 {
            margin-bottom: 15px;
         }        
         .margin-bottom-10 {
            margin-bottom: 10px;
         }
         .margin-bottom-5 {
            margin-bottom: 5px;
         }
        .margin-top-20 {
          margin-top: 20px;
        }
        .margin-top {
          margin-top: 10px;
        }
        .margin-top-5 {
          margin-top: 5px;
        }
        .margin-top-7 {
            margin-top: 7px;
        }
        .margin-right {
          margin-right: 15px;
        }
        .margin-right-small {
          margin-right: 8px;
        }
        .margin-right-5 {
            margin-right: 5
        }
         .right-margin-small {
            margin-right: 15px;
         }
         .right-margin-mid {
            margin-right: 25px;
         }
        .right-margin-big {
            margin-right: 100px;
         }
        .left-margin-3 {
            margin-left; 3px;
        }
         .left-margin-small {
            margin-left: 15px;
         }
         .left-margin-mid {
            margin-left: 25px;
         }
         .small-margin-bottom {
            margin-bottom: 10px;
         }
         .margin=bottom {
            margin-bottom: 15px;
         }
         .larg-margin-bottom {
            margin-bottom: 25px;
         }
         .easy-padding {
            padding: 10px;
         }
         .hard-padding: 20px;
         .quarter-width {
            width: 25%;
         }
         .padding-top {
            padding-top: 2px;
         }
         .gap_status_txt {
            margin-left: 5px;
            padding-top: 7px;
         }
        .half-width {
            width: 50%;
         }
         .full-width {
            width: 100%;
         }
         .wrap {
            overflow-wrap: normal;
         }
         .contain {
            
         }
         .center {
            text-align: center;
         }
         .right {
            text-align: right;
         }
         .clear-decoration {
            text-decoration: none;
         }
         .clear-color {
            color: black !important;
         }
         .inline-block {
            display: inline-block;
         }
         .flx-bx-center {
            display: flex;
            justify-content: center;         
         }
         .flx-bx-start {
            display: flex;
            justify-content: flex-start;
         }
         .flx-bx-end {
            display: flex;
            justify-content: flex-end;
         }
         .flx-bx-space-between {
            display: flex;
            justify-content: space-between;
         }
        .flx-bx-space-around {
            display: flex;
            justify-content: space-around;
         }
        .flx-bx-space-evenly {
            display: flex;
            justify-content: space-evenly;
         }
         /* for testing */
         .outline {
            outline: 1px solid blue;
         }




        /***************************************************
                        MULTI-USE (NO PREFIX)  
            example
            title {font-family: "Times New Roman"                         
        ***************************************************/ 
        .callout {
            border: 1px solid black;
            border-radius: 5px;
            border-shadow: 2 2 2;
            width:25%;
            padding: 25px 10px 25px 10px;
        }
        .data-point-label {
            font-size: 1.2rem;
            font-weight: bold;
            text-align: center;
        }
        .data-point {
            font-size: 1.2rem;
            text-align: center;
        }
        .button {
            color: darkgray;
            background-color: white;
            border: 1px solid black;
            border-radius: 5px;
            border-shadow: 2 2 2;
            padding: 10px 25px 10px 25px;
            text-align: center;
        }
        .button:hover {
            cursor: pointer;
            color: gray;
            background-color: lightgray;
        }
        .float-left {
            float: left;
            margin-left: 15px;
        }
        .float-right {
            float: right;
            margin-right: 15px;
        }
        .clear-left {
            clear: left;
        }
        .clear-right {
            clear: right;
        }
        .clear-both {
            clear: both;
        }
        # .footer-bar {
        #     background-color: #DCDCDC;
        #     height: 20px;
        #     width: 100%;
        #     margin-top: 30px;
        #     margin-bottom:30px;
        #  }
         
        # .footer-bar {
        #     border-bottom: 20px;
        #     background-color: #DCDCDC;
        #     height: 20px;
        #     width: 100%;
        #     margin-top: 30px;
        #     margin-bottom:30px;
        #  }
         
        .footer-bar {
            border: none;
            border-top: 20px dashed #DCDCDC;
            color: #fff;
            background-color: #fff;
            height:1px;
            width: 100%;
        }


        /***************************************************
                                CUSTOM 
                Add 3-char prefix for page or component 
                    Place class under section 

          example of custom class on main page
          /---MAIN PAGE ---/                                 
          mai_subheader_pink { color: pink; font-family: "Times New Roman"}
        ***************************************************/   
        
        .splash_wrapper {
            display: flex;
            flex-direction: center;
            justify-content: center;
            flex-direction: column;
            color: #464D5D;
        }
        .splash_img {
            width: 90%;
            height: 300px;
            object-fit: contain;
        }
        .splash_color {
            color: #464D5D;
        }
        /* ----------------------------------*/
        /**** DETAIL_CARD ****/ 
        /* ----------------------------------*/    
        .det_footer {
            margin-top: 30px;
            margin-botTom: 10px;
            margin-left: 15px;
            # margin-right:20%;
        }
        .det_header{
            # margin-top: 10px;
            # margin-bottom: 10px;
            margin-left: 0px;
            margin-right:10%;
        }
        .dcard_header_status_wrapper {
            display: flex;
            flex-direction: flex-start;
        }
        .dcard_header_status {
            display: flex;
            flex-direction: flex-start;
            align-items: center;
            font-weight: bold;
        }
        .dcard_header_unresolved {
            border: 1px solid gray;
            border-radius: 5px;
            background-color: black;
            color: white;
            padding: 3px 8px 3px 8px;
            font-weight: bold;
        }
        .chk_box_resolved2 {
            display: flex;
            flex-direction: center;
            align-items: center;
            border: 1px solid black;
            border-radius: 3px;
            height: 18px;
            width: 18px;
            margin-right: 3px;
            font-weight: bold;
            color: white;
            text-align: center;
            padding-left: 4px;
            background-color: #fc4c4c;
        }
        .chk_box_resolved {
            display: flex;
            flex-direction: center;
            align-items: center;
            # border: 1px solid black;
            border-radius: 3px;
            height: 18px;
            width: 18px;
            margin-right: 3px;
            font-weight: bold;
            # color: darkgreen;
            text-align: center;
            padding-left: 4px;
            # background-color: #fc4c4c;
        }
        .chk_box_strike_through {
            text-decoration: line-through;
            color: #A9A9A9;
        }
        .chk_box_unresolved {
            display: flex;
            flex-direction: center;
            align-items: center;
            border: 2px solid #acacb4;
            border-radius: 3px;
            height: 18px;
            width: 18px;
            margin-right: 3px;
            font-weight: bold;
            color: white;
            text-align: center;
            padding-left: 4px;
            # background-color: #fc4c4c;
        }
        .det_empty_div_h4 {
            width: 40px;
            height: 38px;
            # outline: 1px solid blue;
        }
        .det_matching_alt_asin {
            height: 38px;
            color: #4d4d00;
            font-style: italic;
            display: flex;
        }
        .det_matching_alt_close_asin {
            height: 38px;
            color: #00394d;
        }
        .det_empty_div {
            width: 40px;
            height: 54px;
            # outline: 1px solid blue;
        }
        .det_margin-bottom {
            margin-bottom: 57px;
        }
        .det-label-tag {
            # padding: 2px 5px 2px 5px;
            # background-color: #696969;
            
            color: #696969;
            # border-radius: 5px;
            font-size: 1rem;
            font-family: "Source Sans Pro", sans-serif;
         }
         .det-change-hist-wrapper {
            margin-bottom: 15px;
         }
         .det-note-wrapper {
            margin-bottom: 5px;
            margin-top: 15px;
         }
         .det-img {
            height: 250px;
            width: 250px;
            object-fit: contain;
         }
         .det_prod_title {
            min-height: 75px;
            width: 100%;
         }
         .det_img_subtitle {
            width: 100%;
         }
        .det_ops_value {
            font-size: 1.2rem;
            # font-weight: bold;
            # color: darkgray;
        }
        /* ----------------------------------*/
        /**** Util Functions ****/ 
        /* ----------------------------------*/    
        .utl_mismatch {
            color: #fc4c4c;
            font-weight: 600; 
        } 
        .utl_match {
            color: #4da64d;
            font-weight: 550; 
            font-family: Verdana;
        }      
         
         
         
         
    /********************************************/
    /*****        NEW DETAIL CARD DESIGN       ****/
    /********************************************/
    .det_outer_wrapper {
      display: flex:;
      flex-direction: column;
      font-family: "Source Sans Pro", sans-serif;
    }
    /********************************************/
    /*****        DETAIL CARD HEADER         ****/
    /********************************************/
    .dcard_header {
      display: flex;
      justify-content: space-between;
      width: 100%;
    }
    .dcard_header_count {
        font-size: 1.75rem;
        font-family: "Source Sans Pro", sans-serif;
        font-weight: 600;
        color: rgb(49, 51, 63);
        line-height: 1.2;
        letter-spacing: -0.005em; 
    }
    .dcard_header_section {
        display: flex;
    }
    /**** STATUS CARD ****/
    .dcard_status_base {
      border: 1px solid black;
      text-align center;
      font-weight: bold;
      padding: 3px 15px 3px 15px;
      border-radius: 5px;
      height: 32px;
      margin-top: 3px;    
    }
    .dcard_resolved_pm {
        background-color: darkgreen; 
        color: white; 
    }
    .dcard_resolved_pbi {
        background-color: green; 
        color: white;
    }
    .dcard_resolved_smpo {
        background-color: lime; 
        color: black; 
    }
    .dcard_resolved_other {
        background-color: lightgreen; 
        color: black; 
    }
    .dcard_header_unresolved {
        color: white;
        background-color: black;
        border: 1px solid white;
    }
    .dcard_header_punt {
        color: white;
        background-color: purple;
    }
    .dcard_header_question {
        color: white;
        background-color: red;
    }
    
    /******************/
    .dcard_header_changes {
      padding: 3px 8px 3px 8px;
      margin-top: 4px;
    }
    .dcard_header_edge {
        padding: 3px 8px 3px 8px;
        margin-top: 4px;
    }
    .dcard_header_chng_unsaved {
        padding: 6px 3px 3px 3px;
        margin-top: 4px;
    }
    .dcard_submit_changes_arrow {
        display: flex;
        justify-content: space-between;
        padding: 6px 3px 3px 3px;
        margin-top: 4px;
        background-color: #FFF0F5;
    }
    .dcard_submit_cancel_holder {
        display: flex;
    }
    .rotate-180 {
        transform: rotate(180deg);
    }
    .dcard_header_tag {
        padding: 3px 8px 3px 8px;
        margin-top: 4px;
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        align-items: center;
    }
    .dcard_header_audits_wrapper  {
      padding: 3px 0px 3px 0px;
      margin-top: 4px;
    }
    .dcard_header_audits_wrapper {
      display: flex;
      flex-wrap: wrap;
    }
    .dcard_header_audit {
      # border: 1px solid darkgray;
      color: #505050;
      text-align: center;      
      font-weight: bold;
      padding: 8px 8px 8px 8px;
      # border-radius: 5px;
      # height: 26px;
      margin-right: 15px;
    }
    /********************************************/
    /*****        DETAIL CARD BODY         ****/
    /********************************************/
    .dcard_body_wrapper {
      display: flex;
      justify-content: space-around;
    }
    .card_body_img_wrapper {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
      margin: 5px;
      border: 1px solid #C0C0C0;
      padding: 5px;
      min-height: 425px;
    }
    .card_body_img_wrapper_empty {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        margin-top: 200px;
    }
    .card_body_img {
      width: 90%;
      height: 300px;
/*      object-fit: fit;*/
      object-fit: contain;
    }
    .card_body_img_catalog {
      font-size: .7rem;
      font-color: gray;
      font-style: italic;
    }
    .card_body_img_details_wrapper {
      display: flex;
      justify-content: space-around;
      width: 100%;
      font-size: 1rem;
    }
    /**** Interpretation Feature ****/
    .gap_status_wrapper {
        display: flex;
        align-item: center;
        justify-content: center;
    }
    .gap_status_img {
        width: 30px;
        height: 30px;
        margin-right: 3px;
    }
    .card_body_img_interpretation_wrapper {
      display: flex;
/*      background-color: #F0F0F0;*/
      /*border: 1px solid gray;
      border-radius: 5px;*/
    }
    .card_body_img_interpretation_img {
      width: 30px;
      height: 30px;
    }
    .card_body_img_interpretation {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .card_body_size_interpretation {
        margin-left: 10px;
    }
    .card_body_img_sic_gap {
      background-color: #DDDDDD;
      padding: 3px 0px 3px 0px;
      color: black;
      border: 1px solid black;
      border-radius: 5px;
      min-width: 150px;
      text-align: center;
    }
    .card_body_img_not_sic_gap {
      padding: 3px 0px 3px 0px;
      color: black;
      border: 1px solid gray;
      border-radius: 5px;
      min-width: 150px;
      text-align: center;
    }
    /**** Matching Bar Feature ****/
    .dcard_match_bar {
      display: flex;
      justify-content: space-between;
      border-bottom: 2px solid black;
      width: 66%;
      margin-left: 17%;
    }
    .dcard_match_bar_mid {
      display: flex;
      justify-content: space-between;
      border-bottom: 2px solid black;
      width: 33%;
      margin-left: 15%;
    }
    .dcard_match_bar_long {
      display: flex;
      justify-content: space-between;
      border-bottom: 2px solid black;
      width: 66%;
      margin-left: 15%;
    }
    # .dcard_no_match {
    #   display: flex;
    #   justify-content: space-between;
    #   width: 33%;
    #   margin-left: 15%;
    # }    
    .dcard_no_match {
      # background-color: black;
      border-top: 3px solid #ff0000;
      border-radius: 5px;
      color: #ff0000;
      # font-weight: bold;
      text-align: center;
      padding-top: 1px;
      padding-bottom: 2px;
      font-size: .9rem;
    }         
    
    /****  PICTURE CARD ****/
    .dcard_id_number_subtext {
        font-size: .9rem;
        color: gray;
        text-decoration: italic;
    }
    
    /**** HTML SYMBOLS ********/
    .html_green_check {
        font-weight: bold;
        color: #048204;
        font-size: 23px;
        margin-left: 3px; 
    }
    .html_orange_check {
        font-weight: bold;
        color: #F98002;
        font-size: 23px;
        margin-left: 3px;     
    }
    .html_red_x {
        font-weight: bold;
        color: red;
        font-size: 29px;
        margin-left: 3px; 
    }
    .html_question {
        font-weight: bold;
        color: gray;
        font-size: 23px;
        margin-left: 3px;    
    }
    .html_n_a{
        font-weight: bold;
        color: #1E3250;
        font-size: 23px; 
        margin-left: 3px;   
    }
    .backup_success {
        color: green;     
    }
    .backup_fail {
        color: red;     
    }
    .data_point_contain {
        word-wrap: break-word;
        max-width: 100%;
    }
    .tags_holder {
        # border: 2px solid black;
        margin-top: 40px;
    }
    .tag_wrapper {
        padding: 5px 8px 5px 8px;
        # background-color: #F8F8F8;
        border: 1px solid lightgray;
        border-radius: 5px;
        text-align: center;
        float: left;
        margin: 5px;
        font-size: 1.0rem;
        font-weight: bold;
        font-family: Helvetica;
        box-shadow: 1px 2px 2px lightgray;
        color: gray;
     }
    .admin_user_color_box_wrapper {
        display: flex;
        align-items: center;
        # padding-top: 1px;
        # padding-bottom: 1px;
        margin-bottom: 17px;
     }   
     .admin_user_color_box {
        width: 18px;
        height: 18px;
        margin-right: 5px;
     }
     /**** Maintenance ****/
     .maintenance_holder {
        border: 1px solid lightgray;
        color: htmlgray;
        margin-top: 45px;
        padding: 15px;
        text-align: center;
     }
     .deprecation_stamp {
        border: 1px solid red;
        padding: 0px 25px 0px 25px;
        font-size: 1.0rem;
        color: red;
        font-weight: bold;
     }
     .out_of_scope_stamp {
        border: 1px solid blue;
        padding: 0px 25px 0px 25px;
        font-size: 1.0rem;
        color: blue;
        font-weight: bold;
     }
     .submission_status_notification {
        font-size: 1.2rem;
        font-weight: bold;
        text-align: center;
     }
     .user_guide {
        text-decoration: none;
        font-size: 1.2rem;
     }

    /**** SUMMARY DASHBOARD TWO ****/
    .dash-stats-wrapper {
        padding: 10px;
        padding-left: 10px;
        padding-right: 10px;
        background-color: #f1f2f4;
        border-radius: 5px;
        margin-bottom: 25px;
    }
    .dash-title {
        font-size: 1.1rem;
        font-weight: bold;
        text-align: center;
    }
    .dash-row {
        display: flex;
        justify-content: space-around;
        margin-top: 8px;
    }
    .bottom-border {
        border-bottom: 1px solid #E0E0E0;
    }
    .right-brdr {
        border-right: 1px solid #E0E0E0;
    }
    .dash-col {
        width: 10%;
    }
    .dash-stand-err {
        color: #696969;
        font-size: .9rem;
        font-style: italic;
        # font-weight: bold;
    }
    </style>
"""