<h1> LHC ION -  injection optics</h1>

<h2>Twiss functions</h2>
The Twiss functions of this configuration are shown in the interactive plot below. You can zoom in or hover over any curve to obtain more information about the function's value at a specific element. The full TFS table is available [here](ps_inj_ion.tfs){target=_blank} and the plot in PDF format [here](ps_inj_ion.pdf){target=_blank}. 

<object width="100%" height="680" data="ps_inj_ion.html"></object> 



<h2>Example scripts</h2>

You can directly open a MAD-X example for this configuration in [SWAN](https://cern.ch/swanserver/cgi-bin/go?projurl=https://gitlab.cern.ch/acc-models/acc-models-ps/raw/master/scenarios/lhc_ion/0_injection/MADX_example_ps_inj_ion.ipynb){target=_blank} or download the necessary files below.

??? "MAD-X example script - [direct download](ps_inj_ion.madx)"
        /**********************************************************************************
        *
        * MAD-X input script for the injection optics of the LHC ion cycle.
        * 22/08/2019 - Alexander Huschauer
        ************************************************************************************/
         
        /******************************************************************
         * Energy and particle type definition
         ******************************************************************/

        BEAM, PARTICLE=Pb54, MASS=0.931494 * 207.976/208., CHARGE=54./208., ENERGY=0.931494 * 207.976/208. + 0.072;
        BRHO      := BEAM->PC * 3.3356 * 208./54.;

        /******************************************************************
         * Call lattice files
         ******************************************************************/

        call, file="../../../ps_mu.seq";
        call, file="../../../ps_ss.seq";
        call, file="../../../ps.str";
        call, file="./ps_inj_ion.str";

        /******************************************************************
         * PTC Twiss
         ******************************************************************/

        use, sequence=PS;
        select, flag=ptc_twiss, column=name,keyword,s,x,px,y,py,t,pt,beta11,alfa11,beta22,alfa22,disp1,disp,disp3,disp4,gamma11,gamma22,mu1,mu2,energy,l,angle,K0L,K0SL,K1L,K1SL,K2L,K2SL,K3L,K3SL,K4L,K4SL,K5L,K5SL,VKICK,HKICK,SLOT_ID;
        ptc_create_universe;
        ptc_create_layout, model=2, method=6, nst=5, exact=true,;
        ptc_twiss,closed_orbit,icase=56,no=4, file = './ps_inj_ion.tfs';
        ptc_end;

        stop;

        ! obtain smooth optics functions by slicing the elements
        use, sequence=PS;
        select, flag=ptc_twiss, column=name,keyword,s,x,px,y,py,t,pt,beta11,alfa11,beta22,alfa22,disp1,disp,disp3,disp4,gamma11,gamma22,mu1,mu2,energy,l,angle,K0L,K0SL,K1L,K1SL,K2L,K2SL,K3L,K3SL,K4L,K4SL,K5L,K5SL,VKICK,HKICK,SLOT_ID;
        ptc_create_universe;
        ptc_create_layout, model=2, method=6, nst=5, exact=true,;
        ptc_twiss,closed_orbit,icase=56,no=4,slice_magnets=true, file = './ps_inj_ion_interpolated.tfs';
        ptc_end;

??? "MAD-X strength file - [direct download](ps_inj_ion.str)"
        /*******************************************************************************
        **                        SBEND K1 and multipoles in MUs                      **
        *******************************************************************************/

        k1_f               =      0.05704335552 ;
        k1_d               =     -0.05709660013 ;
        mpk2               =     -0.01939553022 ;
        mpk2_j             =      0.04111867145 ;
        mpk3_f             =     -0.03795098301 ;
        mpk3_d             =     -0.21745678210 ;

        /*******************************************************************************
        **                                    LEQs                                    **
        *******************************************************************************/

        kf                 =    -0.002346487992 ;
        kd                 =     0.002311566521 ;

        /*******************************************************************************
        **                           Injection bumpers                                **
        ** 		      values taken directly from LSA on 22.08.2019	     			  **
        *******************************************************************************/

        CC206:= 0.00032/(BRHO);

        BSW26 =  21 * CC206;

        RETURN;

??? "MAD-X sequence of straight section elements - [direct download](../../../ps_ss.seq)"
        ! TODO: remove all descriptions starting with ++, as those cause errors in MAD-X
        !++HEAD++
          /**********************************************************************************
          *
          * PS version STUDY in MAD X SEQUENCE format
          * Generated the 07-JUN-2019 18:23:18 from LHCLAYOUT@EDMSDB Database
          *
          * Generated from LHCLAYOUT@EDMSDB since                 10/04/2017 P.Le Roux
          ************************************************************************************/
        ! TODO: remove description
        !++END_HEAD+++

        ! TODO: remove description
        !++ELEMENTS++

        /************************************************************************************/
        /*                       TYPES DEFINITION                                           */
        /************************************************************************************/

        //---------------------- DRIFT          ---------------------------------------------
        BFA       : DRIFT       , L := 1;         ! Bending magnet. Fast bumper
        KFA__001  : DRIFT       , L := 1;         ! Fast Kicker
        KFA__002  : DRIFT       , L := .8;        ! Fast Kicker
        !TODO: correct type of KFA71 and check length
        KFA__003  : HKICKER       , L := 2.4;       ! Fast Kicker
        KFB       : DRIFT       , L := 1;         ! kicker (Damper)
        MCVAAWAP  : DRIFT       , L := .2;        ! Corrector magnet, dipole vertical, type 202
        SEH__001  : DRIFT       , L := 1;         ! Electrostatic septum (ejection).
        SMH__001  : DRIFT       , L := 2.4;       ! Septum Magnet Horizontal
        SMH__003  : DRIFT       , L := .8;        ! Septum Magnet Horizontal
        SMH__004  : DRIFT       , L := 1.2;       ! Septum Magnet Horizontal
        TDI__001  : DRIFT       , L := 1;         ! Internal beam dump (PS)
        //---------------------- HKICKER        ---------------------------------------------
        !TODO: correction of the length
        BLG       : HKICKER     , L := .2;        ! Dipole magnet, bumper horizontal, type 213
        KFA__004  : HKICKER     , L := .888;      ! Fast Kicker
        KFA__005  : HKICKER     , L := 0;         ! Fast Kicker
        MCHBAWWP  : HKICKER     , L := .23;       ! Corrector magnet, dipole horizontal, type 205
        MCHBBWWP  : HKICKER     , L := .27;       ! Corrector magnet, dipole horizontal, type 206
        MDBBBCWP  : HKICKER     , L := .19;       ! Dipole magnet, bumper horizontal, type 209
        MDBCAWWP  : HKICKER     , L := .3;        ! Dipole magnet, bumper vertical, type 210
        SMH__007  : HKICKER     , L := 0;         ! Septum Magnet Horizontal
        //---------------------- INSTRUMENT     ---------------------------------------------
        !TODO: also define as monitor
        MSG       : INSTRUMENT  , L := 0;         ! SEM grid
        //---------------------- MARKER         ---------------------------------------------
        TDIRB001  : MARKER      , L := 0;         ! Internal Beam Dump, Retarding, type B
        TPS       : MARKER      , L := 0;         ! Septum Shielding  (Absorber)
        VVS       : MARKER      , L := 0;         ! Vacuum Sector Valve (PS Complex)
        //---------------------- MONITOR        ---------------------------------------------
        BCT       : MONITOR     , L := 0;         ! Beam current transformer
        BCTF      : MONITOR     , L := 0;         ! Fast Beam Current Transformers
        BCW_A     : MONITOR     , L := 0;         ! Beam Wall Current monitor type A
        BGIHA     : MONITOR     , L := 0;         ! Beam Gas Ionisation Horizontal, type A
        BPMTS     : MONITOR     , L := 1;         ! 2 planes Stripline BPM with 4 long electrodes for PS Tune
        BPUNO     : MONITOR     , L := 0;         ! Beam Position, Normal Pick-up
        BPUWA     : MONITOR     , L := 0;         ! Beam Position Pickup, Wideband, type A
        BSGW      : MONITOR     , L := 0;         ! SEM Grid with Wire
        BTVMA001  : MONITOR     , L := 0;         ! Beam observation TV, with Magnetic coupling, type A, variant 001
        BTVMF005  : MONITOR     , L := 0;         ! Beam TV Motorised Flip, variant 005
        BTVPL001  : MONITOR     , L := 0;         ! Beam observation TV Pneumatic Linear, variant 001
        BWSRB     : MONITOR     , L := 0;         ! Beam Wire Scanner, Rotational, type B
        MTV       : MONITOR     , L := 0;         ! TV screen (scintillation monitor)
        UDP       : MONITOR     , L := 1;         ! Pick-ups  (p.u. electrode). damper
        UFB       : MONITOR     , L := 0;         ! Feedback pick-up.
        ULF       : MONITOR     , L := 0;         ! Low Frequency pick-up
        ULG       : MONITOR     , L := 0;         ! Closed orbit. Large pick-up
        UPH__001  : MONITOR     , L := 0;         ! Pick-up  (p.u. electrode). Beam control, phase.
        URL       : MONITOR     , L := 0;         ! Pick-up  (p.u. electrode). Beam control, radial.
        URP       : MONITOR     , L := 0;         ! Pick-up  (p.u. electrode). Resistive position.
        URS       : MONITOR     , L := 0;         ! Pick-up  (p.u. electrode). Wide band, resistive.(wall current moniteur).
        USP       : MONITOR     , L := 0;         ! Pick-ups  (p.u. electrode). Special (low intensity)

        //---------------------- MULTIPOLE      ---------------------------------------------
        MM_AAIAP  : MULTIPOLE   , L := 0;         ! Multipole magnet, type 403

        !TODO: remove main unit multipoles
        MU_HRCWP  : MULTIPOLE   , L := 4.403185;  ! Main unit, multipole, PS type R
        MU_HSCWP  : MULTIPOLE   , L := 4.403185;  ! Main unit, multipole, PS type S
        MU_HTCWP  : MULTIPOLE   , L := 4.403185;  ! Main unit, multipole, PS type T
        MU_HUCWP  : MULTIPOLE   , L := 4.403185;  ! Main unit, multipole, PS type U

        ! TODO: implement actual magnetic length for each magnetic element
        ! length of type 802 according to MTE design report
        ! verify length of type MTE, closer to 0.5 m (initially 0.48 m) according to specififcations
        //---------------------- OCTUPOLE       ---------------------------------------------
        MONAAFWP  : OCTUPOLE    , L := 0.22;      ! Octupole magnet, type 802
        MONDAFWP  : OCTUPOLE    , L :=  .5;      ! Octupole magnet, type MTE
        //---------------------- PLACEHOLDER    ---------------------------------------------
        !TODO: remove placeholder?
        MDBCCWWC  : PLACEHOLDER , L := .36;       ! Dipole magnet, bumper horizontal, type IPM
        //---------------------- QUADRUPOLE     ---------------------------------------------
        !TODO: verify lengths of elements
        !changed: 409, 
        MQNAAIAP  : QUADRUPOLE  , L := 0;         ! Quadrupole magnet, type 401
        MQNABIAP  : QUADRUPOLE  , L := 0;         ! Quadrupole magnet, type 402
        MQNBAFAP  : QUADRUPOLE  , L := .2;        ! Quadrupole magnet, type 406
        MQNBCAWP  : QUADRUPOLE  , L := .2;        ! Quadrupole magnet, type 407
        MQNBDAAP  : QUADRUPOLE  , L := .2;        ! Quadrupole magnet, type 408
        MQNCAAWP  : QUADRUPOLE  , L := .25;       ! Quadrupole magnet, type 409
        MQNCHAWP  : QUADRUPOLE  , L := .2;        ! Quadrupole magnet, type 414
        MQSAAIAP  : QUADRUPOLE  , L := 0;         ! Quadrupole magnet, skew, type 404
        //---------------------- RFCAVITY       ---------------------------------------------
        AARFB     : RFCAVITY    , L := 1;         ! RF CAVITY 40/80 MHZ

        ! TODO: verify length of 10 MHz cavities, see EDMS 1265845
        ACC10     : RFCAVITY    , L := 2.39;      ! 10 MHz radio frequency cavity

        ! TODO: correct length of 20 MHz cavities to 1.0 m (in LDB also the responsible is incorrect, should be somebody from BE-RF)
        ACC20     : RFCAVITY    , L := 1.0;       ! 20 MHz radio frequency cavity

        ! TODO: correct length of 200 MHz to 0.40 m
        ACC200    : RFCAVITY    , L := .40;       ! RF Cavity 200 MHz

        ! TODO: correct length of 40 MHz cavities to 1.0 m
        ACC40     : RFCAVITY    , L := .99;       ! 40 MHz radio frequency cavity
        ACWFA     : RFCAVITY    , L := .88;       ! Accelerating Cavities - Wide-band - Finemet - Type A (for PSring)
        //---------------------- SEXTUPOLE      ---------------------------------------------
        !TODO: verify magnetic length of type 608 - changed according to MTE design report
        MXNBAFWP  : SEXTUPOLE   , L := .195;        ! Sextupole Magnet, type 608
        MXNCAAWP  : SEXTUPOLE   , L := 0;         ! Sextupole Magnet, type 610
        MX_AAIAP  : SEXTUPOLE   , L := 0;         ! Sextupole Magnet, type 601
        MX_ABIAP  : SEXTUPOLE   , L := 0;         ! Sextupole magnet, type 602

        ! TODO: remove return statement here
        !return;

        ! TODO: remove description
        !++END_ELEMENTS++

        ! TODO: remove description
        !++SEQUENCE++

        /************************************************************************************/
        /*                       PS STRAIGHTSECTION                                         */
        /************************************************************************************/

        PS01: SEQUENCE, L=3;
         PR.XSE01.A     : MXNBAFWP  , AT = .42  , SLOT_ID = 2369746;
         PR.XSE01.B     : MXNBAFWP  , AT = .675 , SLOT_ID = 2369747;
        ENDSEQUENCE;

        PS02: SEQUENCE, L=1.6;
         PA.UFB02       : BPUNO     , AT = .0934, SLOT_ID = 2253327;
         PA.CWB02       : ACWFA     , AT = .775 , SLOT_ID = 10338559;
         PR.MM02        : MM_AAIAP  , AT = 1.47 , SLOT_ID = 8178825;
        ENDSEQUENCE;

        PS03: SEQUENCE, L=1.6;
         PR.BPM03       : BPUNO     , AT = .0934, SLOT_ID = 2253342; ! Position is based on optics definition
         PR.BCW03.A     : BCW_A     , AT = .5137, SLOT_ID = 36269910; ! Position is an estimate
         PR.BCW03.B     : BCW_A     , AT = 1.036, SLOT_ID = 36269911; ! Position is an estimate
         PR.MM03        : MM_AAIAP  , AT = 1.47 , SLOT_ID = 5365801; ! Position is based on optics definition
        ENDSEQUENCE;

        PS04: SEQUENCE, L=1.6;
         PE.KFA04       : KFA__004  , AT = .694 , SLOT_ID = 2369736;
         PR.MM04        : MM_AAIAP  , AT = 1.47 , SLOT_ID = 5365802;
        ENDSEQUENCE;

        PS05: SEQUENCE, L=1.6;
         PR.BPM05       : BPUNO     , AT = .0934, SLOT_ID = 2253375;
         PE.QKE16.05    : MQNCHAWP  , AT = .436 , SLOT_ID = 2253376;
         PR.DHZOC05     : MDBCAWWP  , AT = .929 , SLOT_ID = 8178824;
         PR.QFN05       : MQNAAIAP  , AT = 1.47 , SLOT_ID = 2253379;
        ENDSEQUENCE;

        PS06: SEQUENCE, L=3;
        ! TODO: correct position of PR.QDW06 (should be at the end of PS06 - I have manually inserted it below for the time being)
        ! PR.QDW06       : MQNABIAP  , AT = -14.1, SLOT_ID = 2253399;

        ! TODO: correct positions of 200 MHz cavities, as they are overlapping (where to find proper position information?)
        ! PA.C200.06.A   : ACC200    , AT = .5455, SLOT_ID = 2253393;
        ! PA.C200.06.B   : ACC200    , AT = .9195, SLOT_ID = 2253394;
        ! PA.C200.06.C   : ACC200    , AT = 1.293, SLOT_ID = 2253395;
        ! PA.C200.06.D   : ACC200    , AT = 1.667, SLOT_ID = 2253396;
        ! PA.C200.06.E   : ACC200    , AT = 2.041, SLOT_ID = 2253397;
        ! PA.C200.06.F   : ACC200    , AT = 2.415, SLOT_ID = 2253398; 

         PA.C200.06.A   : ACC200    , AT = .4, SLOT_ID = 2253393;
         PA.C200.06.B   : ACC200    , AT = .8, SLOT_ID = 2253394;
         PA.C200.06.C   : ACC200    , AT = 1.2, SLOT_ID = 2253395;
         PA.C200.06.D   : ACC200    , AT = 1.6, SLOT_ID = 2253396;
         PA.C200.06.E   : ACC200    , AT = 2., SLOT_ID = 2253397;
         PA.C200.06.F   : ACC200    , AT = 2.4, SLOT_ID = 2253398;

         ! TODO: verify position 
         PR.QDW06       : MQNABIAP  , AT = 2.859, SLOT_ID = 2253399;
        ENDSEQUENCE;

        PS07: SEQUENCE, L=1.6;
         PR.BPM07       : ULG       , AT = .0934, SLOT_ID = 2253413;
         PR.XSE07       : MXNCAAWP  , AT = .6252, SLOT_ID = 2253414;
         PR.QTRTB07     : MQNCAAWP  , AT = 1.115, SLOT_ID = 2253416;
         PR.QSK07       : MQSAAIAP  , AT = 1.471, SLOT_ID = 2253417;
        ENDSEQUENCE;

        PS08: SEQUENCE, L=1.6;
         PR.C80.08      : AARFB     , AT = .775 , SLOT_ID = 2253431;
         PR.MM08        : MM_AAIAP  , AT = 1.475, SLOT_ID = 5365803;
        ENDSEQUENCE;

        PS09: SEQUENCE, L=1.6;
         PE.BFA09.P     : BFA       , AT = .775 , SLOT_ID = 2253447;
        ! TODO: remove BFA staircase as it is overlapping with the pedestal and won't be there any more after LS2
        ! PE.BFA09.S     : BFA       , AT = .775 , SLOT_ID = 10413798;
         PR.QFN09       : MQNAAIAP  , AT = 1.459, SLOT_ID = 2253449;
        ENDSEQUENCE;

        PS10: SEQUENCE, L=1.6;
         PR.BPM10       : BPUNO     , AT = .0934, SLOT_ID = 2253463;
         PR.XSK10       : MX_AAIAP  , AT = .78  , SLOT_ID = 10414023; ! Position is approximate
         PR.VVS10       : VVS       , AT = 1.25 , SLOT_ID = 13720377; ! Position is estimated
         PR.QDN10       : MQNAAIAP  , AT = 1.475, SLOT_ID = 2253464;
        ENDSEQUENCE;

        PS11: SEQUENCE, L=3;
         PA.C10.11      : ACC10     , AT = 1.509, SLOT_ID = 2253478;
        ENDSEQUENCE;

        PS12: SEQUENCE, L=1.6;
         PR.UEP12       : ULG       , AT = .0934, SLOT_ID = 2253493;
         PR.RAL12       : TDIRB001  , AT = .3077, SLOT_ID = 8178823;
         PE.BSW12       : MCHBAWWP  , AT = .6990, SLOT_ID = 2253494;
         PR.DVT12       : MCVAAWAP  , AT = .9550, SLOT_ID = 2253495;
        ENDSEQUENCE;

        PS13: SEQUENCE, L=1.6;
         PR.BPM13       : BPUNO     , AT = .0934, SLOT_ID = 2253509;
         PE.KFA13       : KFA__004  , AT = .694 , SLOT_ID = 2369737;
        ENDSEQUENCE;

        PS14: SEQUENCE, L=1.6;
         PR.XSK14       : MX_ABIAP  , AT = .6231, SLOT_ID = 10414025;
         PE.BSW14       : MCHBAWWP  , AT = 1.091, SLOT_ID = 2253524;
        ENDSEQUENCE;

        PS15: SEQUENCE, L=1.6;
         PR.BPM15       : ULG       , AT = .0895, SLOT_ID = 2253538;
         PE.TPS15       : TPS       , AT = .7766, SLOT_ID = 6894625;
        ENDSEQUENCE;

        PS16: SEQUENCE, L=3;
        ! TODO: BTV16 is overlapping with SMH16, changed position to 0.2 m (instead of .3585 m) 
         PE.BTV16       : MTV       , AT = .2, SLOT_ID = 2253555;
         ! TODO: verify position of SMH16 as drawing PS_LM___0042 indicates central position of 1.505 m
         PE.SMH16       : SMH__001  , AT = 1.472, SLOT_ID = 2253556;
        ENDSEQUENCE;

        PS17: SEQUENCE, L=1.6;
         PR.BPM17       : ULG       , AT = .445 , SLOT_ID = 2253570;
         PR.QFW17       : MQNABIAP  , AT = 1.470, SLOT_ID = 2253572;
        ENDSEQUENCE;

        PS18: SEQUENCE, L=1.6;
         PA.UPH18       : UPH__001  , AT = .0934, SLOT_ID = 2253586;
         PR.DHZOC18     : MCHBAWWP  , AT = .4173, SLOT_ID = 2253587;
         PR.QDW18       : MQNABIAP  , AT = 1.469, SLOT_ID = 2253588;
        ENDSEQUENCE;

        PS19: SEQUENCE, L=1.6;
         PE.BSW23.19    : MCHBAWWP  , AT = .6327, SLOT_ID = 2253605;
         PR.QTRDA19     : MQNBAFAP  , AT = 1.033, SLOT_ID = 2253606;
         PR.QSK19       : MQSAAIAP  , AT = 1.480, SLOT_ID = 2253607;
        ENDSEQUENCE;

        PS20: SEQUENCE, L=1.6;
         PR.BPM20       : BPUNO     , AT = .0934, SLOT_ID = 2253621;
         PE.BSW20       : MCHBAWWP  , AT = .4653, SLOT_ID = 2253622;
         PR.VVS20       : VVS       , AT = 1.25 , SLOT_ID = 13720428; ! Position is an estimate
         PR.MM20        : MM_AAIAP  , AT = 1.470, SLOT_ID = 5365804;
        ENDSEQUENCE;

        PS21: SEQUENCE, L=3;
         PE.KFA21       : KFA__004  , AT = 2.094, SLOT_ID = 2369738;
         PR.QFN21       : MQNAAIAP  , AT = 2.859, SLOT_ID = 2253643;
        ENDSEQUENCE;

        PS22: SEQUENCE, L=1.6;
         PA.URL22       : URL       , AT = .0934, SLOT_ID = 2253657;
         PI.BSW26.22    : MCHBBWWP  , AT = .4662, SLOT_ID = 2253658;
         PE.BSW22       : MCHBAWWP  , AT = .7562, SLOT_ID = 2253659;
         PR.DVT22       : MCVAAWAP  , AT = 1.093, SLOT_ID = 2253660;
         PR.QDW22       : MQNABIAP  , AT = 1.491, SLOT_ID = 2253661;
        ENDSEQUENCE;

        PS23: SEQUENCE, L=1.6;
         PR.BPM23       : BPUNO     , AT = .0934, SLOT_ID = 2253675;
         PE.SEH23       : SEH__001  , AT = .7748, SLOT_ID = 2253676;
         PR.QSK23       : MQSAAIAP  , AT = 1.470, SLOT_ID = 2253678;
        ENDSEQUENCE;

        PS24: SEQUENCE, L=1.6;
         PR.DVT24       : MCVAAWAP  , AT = .8146, SLOT_ID = 2253692;
         PR.QSK24       : MQSAAIAP  , AT = 1.471, SLOT_ID = 2253693;
        ENDSEQUENCE;

        PS25: SEQUENCE, L=1.6;
        ! TODO: verify position of PR.BPM25 - I assume it is at the same position as the other PUs (see also EDMS 223648) 
        ! PR.BPM25       : ULG       , AT = -.093, SLOT_ID = 2253707;
         PR.BPM25       : ULG       , AT = .0934, SLOT_ID = 2253707;
         PE.QKE16.25    : MQNCHAWP  , AT = .5206, SLOT_ID = 2253708;
        ENDSEQUENCE;

        PS26: SEQUENCE, L=3;
         PI.SMH26       : SMH__007  , AT = 1.788, SLOT_ID = 2253724;
         PI.BTV26       : BTVPL001  , AT = 1.788, SLOT_ID = 2253725;
         PI.BSF26       : MSG       , AT = 1.788, SLOT_ID = 2253726;
        ENDSEQUENCE;

        PS27: SEQUENCE, L=1.6;
         PR.BPM27       : ULG       , AT = .0934, SLOT_ID = 2253740;
         PR.QTRDA27     : MQNBAFAP  , AT = .4748, SLOT_ID = 2253741;
         PE.BSW23.27    : MCHBAWWP  , AT = 1.105, SLOT_ID = 2253744;
         PR.QFW27       : MQNABIAP  , AT = 1.469, SLOT_ID = 2253745;
        ENDSEQUENCE;

        PS28: SEQUENCE, L=1.6;
         PI.KFA28       : KFA__005  , AT = .775 , SLOT_ID = 2253760;
         PR.QDW28       : MQNABIAP  , AT = 1.471, SLOT_ID = 2253761;
        ENDSEQUENCE;

        PS29: SEQUENCE, L=1.6;
         PR.QSE29       : MQNCAAWP  , AT = .626 , SLOT_ID = 2253775;
         PR.QTRDB29     : MQNBAFAP  , AT = 1.081, SLOT_ID = 2253777;
         PR.QSK29       : MQSAAIAP  , AT = 1.47 , SLOT_ID = 2253778;
        ENDSEQUENCE;

        PS30: SEQUENCE, L=1.6;
         PR.BPM30       : ULG       , AT = .0934, SLOT_ID = 2253792;
         PR.DVT30       : MCVAAWAP  , AT = .5465, SLOT_ID = 2253793;
         PI.BSW26.30    : MCHBBWWP  , AT = .9505, SLOT_ID = 2253794;
         PR.VVS30       : VVS       , AT = 1.21 , SLOT_ID = 13720429; ! Position is an estimate
         PR.QSK30       : MQSAAIAP  , AT = 1.488, SLOT_ID = 2253795;
        ENDSEQUENCE;

        PS31: SEQUENCE, L=3;
         PR.QFW31       : MQNABIAP  , AT = 2.870, SLOT_ID = 2253811;
        ENDSEQUENCE;

        PS32: SEQUENCE, L=1.6;
         PR.UFB32       : UFB       , AT = .2999, SLOT_ID = 2253825; ! Not connected
         PR.QDW32       : MQNABIAP  , AT = 1.471, SLOT_ID = 2253826;
        ENDSEQUENCE;

        PS33: SEQUENCE, L=1.6;
         PR.BPM33       : ULG       , AT = .0934, SLOT_ID = 2253840;
         PI.QLB33       : MQNCHAWP  , AT = .52  , SLOT_ID = 47643341;
         PA.UFB33       : UFB       , AT = 1.18 , SLOT_ID = 2253842; ! Not connected
         PR.QSK33       : MQSAAIAP  , AT = 1.469, SLOT_ID = 2253843;
        ENDSEQUENCE;

        PS34: SEQUENCE, L=1.6;
         PR.BCT34       : BCT       , AT = .775 , SLOT_ID = 2253858;
         PR.MM34        : MM_AAIAP  , AT = 1.470, SLOT_ID = 5365805;
        ENDSEQUENCE;

        PS35: SEQUENCE, L=1.6;
         PR.BPM35       : BPUNO     , AT = .0934, SLOT_ID = 2253874;
         PR.QFN35       : MQNAAIAP  , AT = 1.459, SLOT_ID = 2253877;
        ENDSEQUENCE;

        PS36: SEQUENCE, L=3;
         PA.URL36       : URL       , AT = .0934, SLOT_ID = 2253891;
         PA.C10.36      : ACC10     , AT = 1.475, SLOT_ID = 2253892;
         PR.QDN36       : MQNAAIAP  , AT = 2.863, SLOT_ID = 2253893;
        ENDSEQUENCE;

        PS37: SEQUENCE, L=1.6;
         PR.BPM37       : BPUNO     , AT = .0934, SLOT_ID = 2253907;
         PR.QTRDB37     : MQNBDAAP  , AT = .4407, SLOT_ID = 2253908;
         PA.UPH37       : BPUNO     , AT = 1.180, SLOT_ID = 2253910;
         PR.MM37        : MM_AAIAP  , AT = 1.459, SLOT_ID = 5365806;
        ENDSEQUENCE;

        PS38: SEQUENCE, L=1.6;
         PA.UPH38       : UPH__001  , AT = .0934, SLOT_ID = 2253926;
         PR.BCT38       : BCTF      , AT = .775 , SLOT_ID = 2253927;
         PR.MM38        : MM_AAIAP  , AT = 1.470, SLOT_ID = 5365807;
        ENDSEQUENCE;

        PS39: SEQUENCE, L=1.6;
         PR.XNO39.A     : MXNBAFWP  , AT = .398 , SLOT_ID = 2369739;
         PR.ONO39       : MONDAFWP  , AT = .7745, SLOT_ID = 2369740;
         PR.XNO39.B     : MXNBAFWP  , AT = 1.151, SLOT_ID = 2369741;
         PR.QFN39       : MQNAAIAP  , AT = 1.459, SLOT_ID = 2253944;
        ENDSEQUENCE;

        PS40: SEQUENCE, L=1.6;
         PR.BPM40       : BPUNO     , AT = .0934, SLOT_ID = 2253958;
         PI.BSW40       : MDBBBCWP  , AT = .472 , SLOT_ID = 2253959;
         PR.ODN40       : MONAAFWP  , AT = .802 , SLOT_ID = 2253960;
         PR.VVS40       : VVS       , AT = 1.251, SLOT_ID = 13720430; ! Position is an estimate
         PR.QDN40       : MQNAAIAP  , AT = 1.481, SLOT_ID = 2253961;
        ENDSEQUENCE;

        PS41: SEQUENCE, L=3;
         PR.QTRTA41     : MQNBCAWP  , AT = 1.475, SLOT_ID = 2253976;
         PR.QSK41       : MQSAAIAP  , AT = 2.895, SLOT_ID = 2253977;
        ENDSEQUENCE;

        PS42: SEQUENCE, L=1.6;
         PI.BTV42.A     : BTVMA001  , AT = 0    , SLOT_ID = 42854779;
         !TODO: position to be verified
         PI.BSW42       : MDBBBCWP  , AT = .472 ;
         PI.BSF42       : MSG       , AT = 1.47 , SLOT_ID = 2253993; ! Slot type is to be checked
        ENDSEQUENCE;

        PS43: SEQUENCE, L=1.6;
         PR.BPM43       : ULG       , AT = .0934, SLOT_ID = 2254008;
         PI.BSW43       : MDBBBCWP  , AT = .5362, SLOT_ID = 2254009;
         PR.QSK43       : MQSAAIAP  , AT = 1.495, SLOT_ID = 2254011;
        ENDSEQUENCE;

        PS44: SEQUENCE, L=1.6;
         PI.BSW44       : MDBBBCWP  , AT = 1.073, SLOT_ID = 2254026;
         PR.MM44        : MM_AAIAP  , AT = 1.473, SLOT_ID = 5365808;
        ENDSEQUENCE;

        PS45: SEQUENCE, L=1.6;
         PR.BPM45       : BPUNO     , AT = .0934, SLOT_ID = 2254042;
         PI.KFA45       : KFA__002  , AT = .775 , SLOT_ID = 2254043;
         PR.QFN45       : MQNAAIAP  , AT = 1.459, SLOT_ID = 2254045;
        ENDSEQUENCE;

        PS46: SEQUENCE, L=3;
         PA.C10.46      : ACC10     , AT = 1.475, SLOT_ID = 2254059;
         PR.QDN46       : MQNAAIAP  , AT = 2.873, SLOT_ID = 2254060;
        ENDSEQUENCE;

        PS47: SEQUENCE, L=1.6;
         PR.BPM47       : BPUNO     , AT = .0934, SLOT_ID = 2254074;
         PR.TDI47       : TDI__001  , AT = .775 , SLOT_ID = 2254075;
         PR.QSK47       : MQSAAIAP  , AT = 1.495, SLOT_ID = 2254077;
        ENDSEQUENCE;

        PS48: SEQUENCE, L=1.6;
         PI.BSG48       : BSGW      , AT = .0934, SLOT_ID = 2254091;
         PR.TDI48       : TDI__001  , AT = .775 , SLOT_ID = 2254092;
         PR.QSK48       : MQSAAIAP  , AT = 1.496, SLOT_ID = 2254093;
        ENDSEQUENCE;

        PS49: SEQUENCE, L=1.6;
         PI.QLB49       : MQNCHAWP  , AT = .52  , SLOT_ID = 47643342;
         PR.QTRTA49     : MQNCAAWP  , AT = 1.093, SLOT_ID = 2254108;
         PR.QFN49       : MQNAAIAP  , AT = 1.481, SLOT_ID = 2254109;
        ENDSEQUENCE;

        PS50: SEQUENCE, L=1.6;
         PR.BPM50       : BPUNO     , AT = .0934, SLOT_ID = 2254123;
         PR.ODN50       : MONAAFWP  , AT = .9725, SLOT_ID = 2254124;
         PR.VVS50       : VVS       , AT = 1.302, SLOT_ID = 13720431; ! Position is an estimate
         PR.QDN50       : MQNAAIAP  , AT = 1.470, SLOT_ID = 2254125;
        ENDSEQUENCE;

        PS51: SEQUENCE, L=3;
         PA.URL51       : URL       , AT = .0934, SLOT_ID = 2254139;
         PA.C10.51      : ACC10     , AT = 1.475, SLOT_ID = 2254140;
        ENDSEQUENCE;

        PS52: SEQUENCE, L=1.6;
         PI.BSG52       : BSGW      , AT = .0934, SLOT_ID = 2254155;
         PR.ODN52.A     : MONAAFWP  , AT = .5155, SLOT_ID = 10430397; ! Position is estimated
         PR.XSK52       : MX_AAIAP  , AT = .75  , SLOT_ID = 10414027; ! Position estimated after installation of new octupole in the same straight section
         PR.ODN52.B     : MONAAFWP  , AT = .9955, SLOT_ID = 2254156; ! Position is estimated
         PR.QSK52       : MQSAAIAP  , AT = 1.496, SLOT_ID = 2253994; ! Moved from Section 42 according to ECR: PS-VC-EC-0001
        ENDSEQUENCE;

        PS53: SEQUENCE, L=1.6;
         PR.BPM53       : BPUNO     , AT = .0934, SLOT_ID = 2254170;
         PE.BSW57.53    : MCHBBWWP  , AT = .8333, SLOT_ID = 2254171;
         PR.MM53        : MM_AAIAP  , AT = 1.469, SLOT_ID = 5365809;
        ENDSEQUENCE;

        PS54: SEQUENCE, L=1.6;
         PI.BSG54       : BSGW      , AT = .0934, SLOT_ID = 2254188;
         PR.BPM54       : BPUNO     , AT = .3615, SLOT_ID = 10414030; ! Position is estimated!
         PR.BWSH54      : BWSRB     , AT = .8035, SLOT_ID = 2254189;
         PR.MM54        : MM_AAIAP  , AT = 1.470, SLOT_ID = 5365810;
        ENDSEQUENCE;

        PS55: SEQUENCE, L=1.6;
         PR.BPM55       : BPUNO     , AT = .0934, SLOT_ID = 2254205;
         PR.XNO55.A     : MXNBAFWP  , AT = .3981, SLOT_ID = 2254206; ! Estimated position
         PR.ONO55       : MONDAFWP  , AT = .7746, SLOT_ID = 2369742;
         PR.XNO55.B     : MXNBAFWP  , AT = 1.151, SLOT_ID = 2254207; ! Estimated position
         PR.QFN55       : MQNAAIAP  , AT = 1.459, SLOT_ID = 2254209;
        ENDSEQUENCE;

        PS56: SEQUENCE, L=3;
        ! TODO: position of cavity to be corrected (I assumed the same position as it is for other C10 cavities - tbc)
        ! PA.C10.56      : ACC10     , AT = .775 , SLOT_ID = 2254223;
         PA.C10.56      : ACC10     , AT = 1.475 , SLOT_ID = 2254223;
         PR.QDW56       : MQNABIAP  , AT = 2.859, SLOT_ID = 2254224;
        ENDSEQUENCE;

        PS57: SEQUENCE, L=1.6;
         PR.BPM57       : ULG       , AT = .0934, SLOT_ID = 2254238;
         PE.BTV57       : BTVMF005  , AT = .3584, SLOT_ID = 2254242;
         PE.SMH57       : SMH__003  , AT = .775 , SLOT_ID = 2254240;
         PR.QSK57       : MQSAAIAP  , AT = 1.496, SLOT_ID = 2254241;
        ENDSEQUENCE;

        PS58: SEQUENCE, L=1.6;
         PR.XSK58       : MX_ABIAP  , AT = .755 , SLOT_ID = 10414032; ! Position is an estimate!
         PR.QSK58       : MQSAAIAP  , AT = 1.481, SLOT_ID = 2254256;
        ENDSEQUENCE;

        PS59: SEQUENCE, L=1.6;
        ! TODO: should be PE.BSW57.59
         PR.BSW57.59    : MCHBAWWP  , AT = .4454, SLOT_ID = 2254271;
         PR.QFW59       : MQNABIAP  , AT = 1.470, SLOT_ID = 2254273;
        ENDSEQUENCE;

        PS60: SEQUENCE, L=1.6;
         PR.BPM60       : ULG       , AT = .0934, SLOT_ID = 2254287;
         PR.DHZOC60     : MCHBBWWP  , AT = .434 , SLOT_ID = 2254288;
         PR.XNO60       : MXNBAFWP  , AT = .85  , SLOT_ID = 10428678; ! Position is an estimate
         PR.VVS60       : VVS       , AT = 1.209, SLOT_ID = 13720432; ! Position is an estimate
         PR.QDW60       : MQNABIAP  , AT = 1.475, SLOT_ID = 2254289;
        ENDSEQUENCE;

        PS61: SEQUENCE, L=3;
        ! TODO: verify positions of all elements as they are overlapping (I arbitrarily moved them to avoid overlapping)
        ! TODO: should be PE.BSW57.61
        ! PR.QTRDB61     : MQNBAFAP  , AT = .4323, SLOT_ID = 2254304;
        ! PE.SMH61       : SMH__004  , AT = .995 , SLOT_ID = 2254307;
        ! PR.BSW57.61    : BLG       , AT = 1.855, SLOT_ID = 2254305; 

         PR.QTRDB61     : MQNBAFAP  , AT = .4323, SLOT_ID = 2254304;
         PE.SMH61       : SMH__004  , AT = 1.195 , SLOT_ID = 2254307;
         PR.BSW57.61    : BLG       , AT = 1.955, SLOT_ID = 2254305;
        ENDSEQUENCE;

        ! TODO: include this SS at extraction from LDB even if empty
        PS62: SEQUENCE, L=1.6;
        ENDSEQUENCE;

        PS63: SEQUENCE, L=1.6;
         PR.BPM63       : ULG       , AT = .3685, SLOT_ID = 2254334;
        ENDSEQUENCE;

        PS64: SEQUENCE, L=1.6;
         PR.BPM64       : BPUNO     , AT = .357 , SLOT_ID = 42548391; ! Position is to be checked
         PR.BWSV64      : BWSRB     , AT = .803 , SLOT_ID = 2254349; ! Position is to be confirmed
         PR.MM64        : MM_AAIAP  , AT = 1.470, SLOT_ID = 5365829;
        ENDSEQUENCE;

        PS65: SEQUENCE, L=1.6;
         PR.BPM65       : BPUNO     , AT = .0934, SLOT_ID = 2254365;
         PR.BWSH65      : BWSRB     , AT = .803 , SLOT_ID = 2369743;
        ENDSEQUENCE;

        PS66: SEQUENCE, L=3;
         PA.C10.66      : ACC10     , AT = 1.475, SLOT_ID = 2254380;
        ENDSEQUENCE;

        PS67: SEQUENCE, L=1.6;
         PR.BPM67       : BPUNO     , AT = .0934, SLOT_ID = 2254394;
         ! TODO: should be PE.BSW57.67
         PR.BSW57.67    : MCHBBWWP  , AT = .4422, SLOT_ID = 2254395;
         PR.QFN67       : MQNAAIAP  , AT = 1.469, SLOT_ID = 2254398;
        ENDSEQUENCE;

        PS68: SEQUENCE, L=1.6;
         PA.UPH68       : UPH__001  , AT = .0934, SLOT_ID = 2254412;
         PR.BPM68       : BPUNO     , AT = .357 , SLOT_ID = 10414035;
         PR.BWSH68      : BWSRB     , AT = .803 , SLOT_ID = 10414037;
         PR.QDN68       : MQNAAIAP  , AT = 1.462, SLOT_ID = 2254413;
        ENDSEQUENCE;

        PS69: SEQUENCE, L=1.6;
         PR.BQS69       : ULF       , AT = .0934, SLOT_ID = 2254427;
         PR.QTRDB69     : MQNBDAAP  , AT = 1.160, SLOT_ID = 2254429;
         PR.MM69        : MM_AAIAP  , AT = 1.459, SLOT_ID = 5365811;
        ENDSEQUENCE;

        PS70: SEQUENCE, L=1.6;
         PR.BPM70       : BPUNO     , AT = .0934, SLOT_ID = 2254445;
         PR.ODN70.A     : MONAAFWP  , AT = .6305, SLOT_ID = 10430399; ! Position is an estimate
         PR.ODN70.B     : MONAAFWP  , AT = .978 , SLOT_ID = 2254446;
         PR.VVS70       : VVS       , AT = 1.344, SLOT_ID = 13720433; ! Position is an estimate
         PR.MM70        : MM_AAIAP  , AT = 1.469, SLOT_ID = 5365812;
        ENDSEQUENCE;

        PS71: SEQUENCE, L=3;
         PE.KFA71       : KFA__003  , AT = 1.472, SLOT_ID = 2254462;
         PR.QFN71       : MQNAAIAP  , AT = 2.859, SLOT_ID = 2254464;
        ENDSEQUENCE;

        PS72: SEQUENCE, L=1.6;
         PR.BQS72       : ULF       , AT = .0934, SLOT_ID = 2254478;
         PR.BQL72       : BPMTS     , AT = .775 , SLOT_ID = 6078900;
         PR.QDN72       : MQNAAIAP  , AT = 1.472, SLOT_ID = 2254479;
        ENDSEQUENCE;

        PS73: SEQUENCE, L=1.6;
         PR.BPM73       : BPUNO     , AT = .0934, SLOT_ID = 2254493;
         PR.QTRTA73     : MQNBCAWP  , AT = .4542, SLOT_ID = 2254494;
         PR.QSK73       : MQSAAIAP  , AT = 1.469, SLOT_ID = 2254497;
        ENDSEQUENCE;

        PS74: SEQUENCE, L=1.6;
         PR.MM74        : MM_AAIAP  , AT = 1.467, SLOT_ID = 5365813;
        ENDSEQUENCE;

        PS75: SEQUENCE, L=1.6;
         PR.BPM75       : BPUNO     , AT = .0934, SLOT_ID = 2254526;
        ENDSEQUENCE;

        PS76: SEQUENCE, L=3;
         PA.URL76       : URL       , AT = .0934, SLOT_ID = 10410423;
         PA.C10.76      : ACC10     , AT = 1.475, SLOT_ID = 2254542;
         PR.MM76        : MM_AAIAP  , AT = 2.872, SLOT_ID = 5365830;
        ENDSEQUENCE;

        PS77: SEQUENCE, L=1.6;
         PR.BPM77       : BPUNO     , AT = .0934, SLOT_ID = 2254558;
         PA.C40.77      : ACC40     , AT = .775 , SLOT_ID = 2254560;
         PR.QFN77       : MQNAAIAP  , AT = 1.481, SLOT_ID = 2254561;
        ENDSEQUENCE;

        PS78: SEQUENCE, L=1.6;
         PA.C40.78      : ACC40     , AT = .775 , SLOT_ID = 2254575;
         PR.QDN78       : MQNAAIAP  , AT = 1.472, SLOT_ID = 2254576;
        ENDSEQUENCE;

        PS79: SEQUENCE, L=1.6;
         PE.KFA79       : KFA__001  , AT = .696 , SLOT_ID = 2254591;
         PR.VVS79       : VVS       , AT = 1.25 , SLOT_ID = 13720434; ! Position is an estimate
         PR.MM79        : MM_AAIAP  , AT = 1.472, SLOT_ID = 5365814;
        ENDSEQUENCE;

        PS80: SEQUENCE, L=1.6;
         PR.BPM80       : BPUNO     , AT = .0934, SLOT_ID = 2254607;
         PA.C20.80      : ACC20     , AT = .775 , SLOT_ID = 2254608;
         PR.MM80        : MM_AAIAP  , AT = 1.472, SLOT_ID = 5365815;
        ENDSEQUENCE;

        PS81: SEQUENCE, L=3;
         PA.C10.81      : ACC10     , AT = 1.475, SLOT_ID = 2254624;
         PR.QFN81       : MQNAAIAP  , AT = 2.881, SLOT_ID = 2254626;
        ENDSEQUENCE;

        PS82: SEQUENCE, L=1.6;
        ! TODO: the BGI magnet and detector are overlapping here. I think it would be best to remove the magnet and only include the instrument PS.BGI82 in the sequence.
        ! PR.MDB82       : MDBCCWWC  , AT = .775 , SLOT_ID = 41442239; ! Position is not mechancially accurate, and based upon being at the centre of the optics defined straight section
         PR.BGI82       : BGIHA     , AT = .775 , SLOT_ID = 41479404; ! Position is not mechanically accurate. Placed at the centre of the optics defined straight section.
         PR.QDN82       : MQNAAIAP  , AT = 1.480, SLOT_ID = 2254641;
        ENDSEQUENCE;

        PS83: SEQUENCE, L=1.6;
         PR.BPM83       : ULG       , AT = .0934, SLOT_ID = 2254655;
         PR.USP83       : USP       , AT = .775 , SLOT_ID = 2254656;
         PR.MM83        : MM_AAIAP  , AT = 1.472, SLOT_ID = 5365816;
        ENDSEQUENCE;

        PS84: SEQUENCE, L=1.6;
         PR.MM84        : MM_AAIAP  , AT = 1.480, SLOT_ID = 5365817;
        ENDSEQUENCE;

        PS85: SEQUENCE, L=1.6;
         PR.BPM85       : ULG       , AT = .0934, SLOT_ID = 2254689;
         PR.BWSV85      : BWSRB     , AT = .803 , SLOT_ID = 2254690;
         PR.QFN85       : MQNAAIAP  , AT = 1.481, SLOT_ID = 2254692;
        ENDSEQUENCE;

        PS86: SEQUENCE, L=3;
         PA.C10.86      : ACC10     , AT = 1.475, SLOT_ID = 2254706;
         PR.QDN86       : MQNAAIAP  , AT = 2.880, SLOT_ID = 2254707;
        ENDSEQUENCE;

        PS87: SEQUENCE, L=1.6;
         PR.BPM87       : BPUNO     , AT = .0934, SLOT_ID = 2254721;
         PR.QTRDA87     : MQNBDAAP  , AT = .4167, SLOT_ID = 2254722;
         PR.QSE87       : MQNCAAWP  , AT = .843 , SLOT_ID = 2254724;
         PR.MM87        : MM_AAIAP  , AT = 1.472, SLOT_ID = 5365818;
        ENDSEQUENCE;

        PS88: SEQUENCE, L=1.6;
         PA.UPH88       : UPH__001  , AT = .0934, SLOT_ID = 2254740;
         PR.C80.88      : AARFB     , AT = .775 , SLOT_ID = 2254741;
         PR.MM88        : MM_AAIAP  , AT = 1.481, SLOT_ID = 5365819;
        ENDSEQUENCE;

        PS89: SEQUENCE, L=1.6;
         PR.C80.89      : AARFB     , AT = .775 , SLOT_ID = 2254758;
         PR.QFN89       : MQNAAIAP  , AT = 1.481, SLOT_ID = 2254759;
        ENDSEQUENCE;

        PS90: SEQUENCE, L=1.6;
         PR.BPM90       : BPUNO     , AT = .0934, SLOT_ID = 2254773;
         PR.BPMW90      : BPUWA     , AT = .4216, SLOT_ID = 42401369; ! Absolute position is not mechanically accurate. It is positioned using the design drawings of the section, and using the optics file position for the centre of PR.ODN90 as the cumulative distance reference
         PR.ODN90       : MONAAFWP  , AT = .9892, SLOT_ID = 2254774;
         PR.VVS90       : VVS       , AT = 1.251, SLOT_ID = 13720435; ! Position is an estimate
         PR.QDN90       : MQNAAIAP  , AT = 1.472, SLOT_ID = 2254775;
        ENDSEQUENCE;

        PS91: SEQUENCE, L=3;
         PA.C10.91      : ACC10     , AT = 1.475, SLOT_ID = 2254789;
         PR.MM91        : MM_AAIAP  , AT = 2.881, SLOT_ID = 5365820;
        ENDSEQUENCE;

        PS92: SEQUENCE, L=1.6;
         PR.C20.92      : ACC20     , AT = .775 , SLOT_ID = 2254806;
         PR.QSK92       : MQSAAIAP  , AT = 1.503, SLOT_ID = 2254807;
        ENDSEQUENCE;

        PS93: SEQUENCE, L=1.6;
         PR.BPM93       : ULG       , AT = .0934, SLOT_ID = 2254821;
         PR.USP93       : UDP       , AT = .775 , SLOT_ID = 2254822;
         PR.QSK93       : MQSAAIAP  , AT = 1.495, SLOT_ID = 2254824;
        ENDSEQUENCE;

        PS94: SEQUENCE, L=1.6;
         PR.XNO94       : MXNBAFWP  , AT = .7706, SLOT_ID = 10428460; ! Position is an estimate
         PR.UWB94       : BPUWA     , AT = 1.125, SLOT_ID = 2254839;
         PR.MM94        : MM_AAIAP  , AT = 1.480, SLOT_ID = 5365821;
        ENDSEQUENCE;

        PS95: SEQUENCE, L=1.6;
         PR.BPM95       : BPUNO     , AT = .0934, SLOT_ID = 2254855;
         PR.UWB95       : URS       , AT = .4624, SLOT_ID = 2254856;
         PR.QTRDA95     : MQNBDAAP  , AT = 1.122, SLOT_ID = 2254858;
         PR.QFN95       : MQNAAIAP  , AT = 1.481, SLOT_ID = 2254859;
        ENDSEQUENCE;

        PS96: SEQUENCE, L=3;
         PA.URL96       : URL       , AT = .0934, SLOT_ID = 2254873;
         PA.C10.96      : ACC10     , AT = 1.475, SLOT_ID = 2254874;
         PR.QDN96       : MQNAAIAP  , AT = 2.880, SLOT_ID = 2254875;
        ENDSEQUENCE;

        PS97: SEQUENCE, L=1.6;
         PR.BPM97       : BPUNO     , AT = .0934, SLOT_ID = 2254889;
         PR.KFB97       : KFB       , AT = .775 , SLOT_ID = 2254890;
         PR.MM97        : MM_AAIAP  , AT = 1.481, SLOT_ID = 5365822;
        ENDSEQUENCE;

        PS98: SEQUENCE, L=1.6;
         PR.UFB98       : BPUNO     , AT = .0934, SLOT_ID = 2254907;
         PR.MM98        : MM_AAIAP  , AT = 1.473, SLOT_ID = 5365823;
        ENDSEQUENCE;

        PS99: SEQUENCE, L=1.6;
         PR.QTRTB99.A   : MQNBCAWP  , AT = .6532, SLOT_ID = 2254926;
         PR.QTRTB99.B   : MQNBCAWP  , AT = 1.078, SLOT_ID = 5706126;
         PR.QFN99       : MQNAAIAP  , AT = 1.472, SLOT_ID = 2254927;
        ENDSEQUENCE;

        PS00: SEQUENCE, L=1.6;
         PR.BPM00       : BPUNO     , AT = .0934, SLOT_ID = 2254941;
         PR.WCM00       : URP       , AT = .5092, SLOT_ID = 2254942;
         PR.ODN00       : MONAAFWP  , AT = .9508, SLOT_ID = 2254943;
         PR.VVS00       : VVS       , AT = 1.251, SLOT_ID = 13720436; ! Position is an estimate
         PR.QDN00       : MQNAAIAP  , AT = 1.472, SLOT_ID = 2254944;
        ENDSEQUENCE;


        /************************************************************************************/
        /*                       PS Sectors                                                 */
        /************************************************************************************/

        ! TODO: modify incorrect MU lengths in LDB to avoid that the magnet is positioned at 3.0000000005
        ! TODO: remove SLOT_IDs for sequence descriptions (PSXX and PR.BHXXX) as SLOT_ID only exists for elements but not for sequences in MAD-X
        ! TODO: modify length of each sector to be 62.83185 instead of 62.831853
        ! TODO: correct positions of SS and BH*

        SEC01 : SEQUENCE, REFER=ENTRY, L = 62.83185;
         PS01      , AT = 0.          ;!, SLOT_ID = 2194390;
         PR.BHT01  , AT = 3.          ;!, SLOT_ID = 2253018;
         PS02      , AT = 7.403185    ;!, SLOT_ID = 2194392;
         PR.BHU02  , AT = 9.003185    ;!, SLOT_ID = 2253020;
         PS03      , AT = 13.40637    ;!, SLOT_ID = 2194394;
         PR.BHT03  , AT = 15.00637    ;!, SLOT_ID = 2253022;
         PS04      , AT = 19.409555   ;!, SLOT_ID = 2194396;
         PR.BHR04  , AT = 21.009555   ;!, SLOT_ID = 2253024;
         PS05      , AT = 25.41274    ;!, SLOT_ID = 2194398;
         PR.BHT05  , AT = 27.01274    ;!, SLOT_ID = 2253026;
         PS06      , AT = 31.415925   ;!, SLOT_ID = 2194400;
         PR.BHR06  , AT = 34.415925   ;!, SLOT_ID = 2253028;
         PS07      , AT = 38.81911    ;!, SLOT_ID = 2194402;
         PR.BHS07  , AT = 40.41911    ;!, SLOT_ID = 2253030;
         PS08      , AT = 44.822295   ;!, SLOT_ID = 2194404;
         PR.BHR08  , AT = 46.422295   ;!, SLOT_ID = 2253032;
         PS09      , AT = 50.82548    ;!, SLOT_ID = 2194406;
         PR.BHT09  , AT = 52.42548    ;!, SLOT_ID = 2253034;
         PS10      , AT = 56.828665   ;!, SLOT_ID = 2194408;
         PR.BHR10  , AT = 58.428665   ;!, SLOT_ID = 2253036;
        ENDSEQUENCE;

        SEC02 : SEQUENCE, REFER=ENTRY, L = 62.83185;
         PS11      , AT = 0.          ;!, SLOT_ID = 2194410;
         PR.BHS11  , AT = 3.          ;!, SLOT_ID = 2253038;
         PS12      , AT = 7.403185    ;!, SLOT_ID = 2194412;
         PR.BHR12  , AT = 9.003185    ;!, SLOT_ID = 2253040;
         PS13      , AT = 13.40637    ;!, SLOT_ID = 2194414;
         PR.BHS13  , AT = 15.00637    ;!, SLOT_ID = 2253042;
         PS14      , AT = 19.409555   ;!, SLOT_ID = 2194416;
         PR.BHU14  , AT = 21.009555   ;!, SLOT_ID = 2253044;
         PS15      , AT = 25.41274    ;!, SLOT_ID = 2194418;
         PR.BHT15  , AT = 27.01274    ;!, SLOT_ID = 2253046;
         PS16      , AT = 31.415925   ;!, SLOT_ID = 2194420;
         PR.BHU16  , AT = 34.415925   ;!, SLOT_ID = 2253048;
         PS17      , AT = 38.81911    ;!, SLOT_ID = 2194422;
         PR.BHT17  , AT = 40.41911    ;!, SLOT_ID = 2253050;
         PS18      , AT = 44.822295   ;!, SLOT_ID = 2194424;
         PR.BHU18  , AT = 46.422295   ;!, SLOT_ID = 2253052;
         PS19      , AT = 50.82548    ;!, SLOT_ID = 2194426;
         PR.BHS19  , AT = 52.42548    ;!, SLOT_ID = 2253054;
         PS20      , AT = 56.828665   ;!, SLOT_ID = 2194428;
         PR.BHR20  , AT = 58.428665   ;!, SLOT_ID = 2253056;
        ENDSEQUENCE;

        SEC03 : SEQUENCE, REFER=ENTRY, L = 62.83185;
         PS21      , AT = 0.          ;!, SLOT_ID = 2194430;
         PR.BHT21  , AT = 3.          ;!, SLOT_ID = 2253058;
         PS22      , AT = 7.403185    ;!, SLOT_ID = 2194432;
         PR.BHR22  , AT = 9.003185    ;!, SLOT_ID = 2253060;
         PS23      , AT = 13.40637    ;!, SLOT_ID = 2194434;
         PR.BHT23  , AT = 15.00637    ;!, SLOT_ID = 2253062;
         PS24      , AT = 19.409555   ;!, SLOT_ID = 2194436;
         PR.BHU24  , AT = 21.009555   ;!, SLOT_ID = 2253064;
         PS25      , AT = 25.41274    ;!, SLOT_ID = 2194438;
         PR.BHT25  , AT = 27.01274    ;!, SLOT_ID = 2253066;
         PS26      , AT = 31.415925   ;!, SLOT_ID = 2194440;
         PR.BHR26  , AT = 34.415925   ;!, SLOT_ID = 2253068;
         PS27      , AT = 38.81911    ;!, SLOT_ID = 2194442;
         PR.BHS27  , AT = 40.41911    ;!, SLOT_ID = 2253070;
         PS28      , AT = 44.822295   ;!, SLOT_ID = 2194444;
         PR.BHU28  , AT = 46.422295   ;!, SLOT_ID = 2253072;
         PS29      , AT = 50.82548    ;!, SLOT_ID = 2194446;
         PR.BHT29  , AT = 52.42548    ;!, SLOT_ID = 2253074;
         PS30      , AT = 56.828665   ;!, SLOT_ID = 2194448;
         PR.BHR30  , AT = 58.428665   ;!, SLOT_ID = 2253076;
        ENDSEQUENCE;

        SEC04 : SEQUENCE, REFER=ENTRY, L = 62.83185;
         PS31      , AT = 0.          ;!, SLOT_ID = 2194450;
         PR.BHT31  , AT = 3.          ;!, SLOT_ID = 2253078;
         PS32      , AT = 7.403185    ;!, SLOT_ID = 2194452;
         PR.BHR32  , AT = 9.003185    ;!, SLOT_ID = 2253080;
         PS33      , AT = 13.40637    ;!, SLOT_ID = 2194454;
         PR.BHS33  , AT = 15.00637    ;!, SLOT_ID = 2253082;
         PS34      , AT = 19.409555   ;!, SLOT_ID = 2194456;
         PR.BHR34  , AT = 21.009555   ;!, SLOT_ID = 2253084;
         PS35      , AT = 25.41274    ;!, SLOT_ID = 2194458;
         PR.BHT35  , AT = 27.01274    ;!, SLOT_ID = 2253086;
         PS36      , AT = 31.415925   ;!, SLOT_ID = 2194460;
         PR.BHR36  , AT = 34.415925   ;!, SLOT_ID = 2253088;
         PS37      , AT = 38.81911    ;!, SLOT_ID = 2194462;
         PR.BHT37  , AT = 40.41911    ;!, SLOT_ID = 2253090;
         PS38      , AT = 44.822295   ;!, SLOT_ID = 2194464;
         PR.BHR38  , AT = 46.422295   ;!, SLOT_ID = 2253092;
         PS39      , AT = 50.82548    ;!, SLOT_ID = 2194466;
         PR.BHT39  , AT = 52.42548    ;!, SLOT_ID = 2253094;
         PS40      , AT = 56.828665   ;!, SLOT_ID = 2194468;
         PR.BHU40  , AT = 58.428665   ;!, SLOT_ID = 2253096;
        ENDSEQUENCE;

        SEC05 : SEQUENCE, REFER=ENTRY, L = 62.83185;
         PS41      , AT = 0.          ;!, SLOT_ID = 2194470;
         PR.BHT41  , AT = 3.          ;!, SLOT_ID = 2253098;
         PS42      , AT = 7.403185    ;!, SLOT_ID = 2194472;
         PR.BHR42  , AT = 9.003185    ;!, SLOT_ID = 2253100;
         PS43      , AT = 13.40637    ;!, SLOT_ID = 2194474;
         PR.BHT43  , AT = 15.00637    ;!, SLOT_ID = 2253102;
         PS44      , AT = 19.409555   ;!, SLOT_ID = 2194476;
         PR.BHR44  , AT = 21.009555   ;!, SLOT_ID = 2253104;
         PS45      , AT = 25.41274    ;!, SLOT_ID = 2194478;
         PR.BHT45  , AT = 27.01274    ;!, SLOT_ID = 2253106;
         PS46      , AT = 31.415925   ;!, SLOT_ID = 2194480;
         PR.BHR46  , AT = 34.415925   ;!, SLOT_ID = 2253108;
         PS47      , AT = 38.81911    ;!, SLOT_ID = 2194482;
         PR.BHS47  , AT = 40.41911    ;!, SLOT_ID = 2253110;
         PS48      , AT = 44.822295   ;!, SLOT_ID = 2194484;
         PR.BHR48  , AT = 46.422295   ;!, SLOT_ID = 2253112;
         PS49      , AT = 50.82548    ;!, SLOT_ID = 2194486;
         PR.BHT49  , AT = 52.42548    ;!, SLOT_ID = 2253114;
         PS50      , AT = 56.828665   ;!, SLOT_ID = 2194488;
         PR.BHR50  , AT = 58.428665   ;!, SLOT_ID = 2253116;
        ENDSEQUENCE;

        SEC06 : SEQUENCE, REFER=ENTRY, L = 62.83185;
         PS51      , AT = 0.          ;!, SLOT_ID = 2194490;
         PR.BHT51  , AT = 3.          ;!, SLOT_ID = 2253118;
         PS52      , AT = 7.403185    ;!, SLOT_ID = 2194492;
         PR.BHR52  , AT = 9.003185    ;!, SLOT_ID = 2253120;
         PS53      , AT = 13.40637    ;!, SLOT_ID = 2194494;
         PR.BHS53  , AT = 15.00637    ;!, SLOT_ID = 2253122;
         PS54      , AT = 19.409555   ;!, SLOT_ID = 2194496;
         PR.BHR54  , AT = 21.009555   ;!, SLOT_ID = 2253124;
         PS55      , AT = 25.41274    ;!, SLOT_ID = 2194498;
         PR.BHT55  , AT = 27.01274    ;!, SLOT_ID = 2253126;
         PS56      , AT = 31.415925   ;!, SLOT_ID = 2194500;
         PR.BHU56  , AT = 34.415925   ;!, SLOT_ID = 2253128;
         PS57      , AT = 38.81911    ;!, SLOT_ID = 2194502;
         PR.BHT57  , AT = 40.41911    ;!, SLOT_ID = 2253130;
         PS58      , AT = 44.822295   ;!, SLOT_ID = 2194504;
         PR.BHU58  , AT = 46.422295   ;!, SLOT_ID = 2253132;
         PS59      , AT = 50.82548    ;!, SLOT_ID = 2194506;
         PR.BHT59  , AT = 52.42548    ;!, SLOT_ID = 2253134;
         PS60      , AT = 56.828665   ;!, SLOT_ID = 2194508;
         PR.BHU60  , AT = 58.428665   ;!, SLOT_ID = 2253136;
        ENDSEQUENCE;

        SEC07 : SEQUENCE, REFER=ENTRY, L = 62.83185;
         PS61      , AT = 0.          ;!, SLOT_ID = 2194510;
         PR.BHT61  , AT = 3.          ;!, SLOT_ID = 2253138;
         PS62	   , AT = 7.403185    ;!;
         PR.BHU62  , AT = 9.003185    ;!, SLOT_ID = 2253140;
         PS63      , AT = 13.40637    ;!, SLOT_ID = 2194514;
         PR.BHT63  , AT = 15.00637    ;!, SLOT_ID = 2253142;
         PS64      , AT = 19.409555   ;!, SLOT_ID = 2194516;
         PR.BHU64  , AT = 21.009555   ;!, SLOT_ID = 2253144;
         PS65      , AT = 25.41274    ;!, SLOT_ID = 2194518;
         PR.BHT65  , AT = 27.01274    ;!, SLOT_ID = 2253146;
         PS66      , AT = 31.415925   ;!, SLOT_ID = 2194520;
         PR.BHR66  , AT = 34.415925   ;!, SLOT_ID = 2253148;
         PS67      , AT = 38.81911    ;!, SLOT_ID = 2194522;
         PR.BHS67  , AT = 40.41911    ;!, SLOT_ID = 2253150;
         PS68      , AT = 44.822295   ;!, SLOT_ID = 2194524;
         PR.BHU68  , AT = 46.422295   ;!, SLOT_ID = 2253152;
         PS69      , AT = 50.82548    ;!, SLOT_ID = 2194526;
         PR.BHT69  , AT = 52.42548    ;!, SLOT_ID = 2253154;
         PS70      , AT = 56.828665   ;!, SLOT_ID = 2194528;
         PR.BHR70  , AT = 58.428665   ;!, SLOT_ID = 2253156;
        ENDSEQUENCE;

        SEC08 : SEQUENCE, REFER=ENTRY, L = 62.83185;
         PS71      , AT = 0.          ;!, SLOT_ID = 2194530;
         PR.BHT71  , AT = 3.          ;!, SLOT_ID = 2253158;
         PS72      , AT = 7.403185    ;!, SLOT_ID = 2194532;
         PR.BHR72  , AT = 9.003185    ;!, SLOT_ID = 2253160;
         PS73      , AT = 13.40637    ;!, SLOT_ID = 2194534;
         PR.BHS73  , AT = 15.00637    ;!, SLOT_ID = 2253162;
         PS74      , AT = 19.409555   ;!, SLOT_ID = 2194536;
         PR.BHU74  , AT = 21.009555   ;!, SLOT_ID = 2253164;
         PS75      , AT = 25.41274    ;!, SLOT_ID = 2194538;
         PR.BHT75  , AT = 27.01274    ;!, SLOT_ID = 2253166;
         PS76      , AT = 31.415925   ;!, SLOT_ID = 2194540;
         PR.BHR76  , AT = 34.415925   ;!, SLOT_ID = 2253168;
         PS77      , AT = 38.81911    ;!, SLOT_ID = 2194542;
         PR.BHT77  , AT = 40.41911    ;!, SLOT_ID = 2253170;
         PS78      , AT = 44.822295   ;!, SLOT_ID = 2194544;
         PR.BHR78  , AT = 46.422295   ;!, SLOT_ID = 2253172;
         PS79      , AT = 50.82548    ;!, SLOT_ID = 2194546;
         PR.BHS79  , AT = 52.42548    ;!, SLOT_ID = 2253174;
         PS80      , AT = 56.828665   ;!, SLOT_ID = 2194548;
         PR.BHR80  , AT = 58.428665   ;!, SLOT_ID = 2253176;
        ENDSEQUENCE;

        SEC09 : SEQUENCE, REFER=ENTRY, L = 62.83185;
         PS81      , AT = 0.          ;!, SLOT_ID = 2194550;
         PR.BHT81  , AT = 3.          ;!, SLOT_ID = 2253178;
         PS82      , AT = 7.403185    ;!, SLOT_ID = 2194552;
         PR.BHR82  , AT = 9.003185    ;!, SLOT_ID = 2253180;
         PS83      , AT = 13.40637    ;!, SLOT_ID = 2194554;
         PR.BHS83  , AT = 15.00637    ;!, SLOT_ID = 2253182;
         PS84      , AT = 19.409555   ;!, SLOT_ID = 2194556;
         PR.BHR84  , AT = 21.009555   ;!, SLOT_ID = 2253184;
         PS85      , AT = 25.41274    ;!, SLOT_ID = 2194558;
         PR.BHT85  , AT = 27.01274    ;!, SLOT_ID = 2253186;
         PS86      , AT = 31.415925   ;!, SLOT_ID = 2194560;
         PR.BHR86  , AT = 34.415925   ;!, SLOT_ID = 2253188;
         PS87      , AT = 38.81911    ;!, SLOT_ID = 2194562;
         PR.BHS87  , AT = 40.41911    ;!, SLOT_ID = 2253190;
         PS88      , AT = 44.822295   ;!, SLOT_ID = 2194564;
         PR.BHU88  , AT = 46.422295   ;!, SLOT_ID = 2253192;
         PS89      , AT = 50.82548    ;!, SLOT_ID = 2194566;
         PR.BHT89  , AT = 52.42548    ;!, SLOT_ID = 2253194;
         PS90      , AT = 56.828665   ;!, SLOT_ID = 2194568;
         PR.BHR90  , AT = 58.428665   ;!, SLOT_ID = 2253196;
        ENDSEQUENCE;

        SEC00 : SEQUENCE, REFER=ENTRY, L = 62.83185;
         PS91      , AT = 0.          ;!, SLOT_ID = 2194570;
         PR.BHT91  , AT = 3.          ;!, SLOT_ID = 2253198;
         PS92      , AT = 7.403185    ;!, SLOT_ID = 2194572;
         PR.BHR92  , AT = 9.003185    ;!, SLOT_ID = 2253200;
         PS93      , AT = 13.40637    ;!, SLOT_ID = 2194574;
         PR.BHS93  , AT = 15.00637    ;!, SLOT_ID = 2253202;
         PS94      , AT = 19.409555   ;!, SLOT_ID = 2194576;
         PR.BHR94  , AT = 21.009555   ;!, SLOT_ID = 2253204;
         PS95      , AT = 25.41274    ;!, SLOT_ID = 2194578;
         PR.BHT95  , AT = 27.01274    ;!, SLOT_ID = 2253206;
         PS96      , AT = 31.415925   ;!, SLOT_ID = 2194580;
         PR.BHR96  , AT = 34.415925   ;!, SLOT_ID = 2253208;
         PS97      , AT = 38.81911    ;!, SLOT_ID = 2194582;
         PR.BHT97  , AT = 40.41911    ;!, SLOT_ID = 2253210;
         PS98      , AT = 44.822295   ;!, SLOT_ID = 2194584;
         PR.BHR98  , AT = 46.422295   ;!, SLOT_ID = 2253212;
         PS99      , AT = 50.82548    ;!, SLOT_ID = 2194586;
         PR.BHS99  , AT = 52.42548    ;!, SLOT_ID = 2253214;
         PS00      , AT = 56.828665   ;!, SLOT_ID = 2194588;
         PR.BHR00  , AT = 58.428665   ;!, SLOT_ID = 2253216;
        ENDSEQUENCE;


        /************************************************************************************/
        /*                       PS Sequence                                                */
        /************************************************************************************/

        ! TODO: account for the initial offset of -0.3 m in LDB (also to be agreed with SU)
        ! TODO: remove SLOT_IDs for sequence descriptions (PSXX and PR.BHXXX) as SLOT_ID only exists for elements but not for sequences in MAD-X
        ! TODO: correct positions of sectors

        PS : SEQUENCE, REFER=ENTRY, L = 628.3185;
         SEC01, AT = 0.0          ;!, SLOT_ID = 2186614;
         SEC02, AT = 62.83185     ;!, SLOT_ID = 2186615;
         SEC03, AT = 125.6637     ;!, SLOT_ID = 2186616;
         SEC04, AT = 188.49555    ;!, SLOT_ID = 2186617;
         SEC05, AT = 251.3274     ;!, SLOT_ID = 2186618;
         SEC06, AT = 314.15925    ;!, SLOT_ID = 2186619;
         SEC07, AT = 376.9911     ;!, SLOT_ID = 2186620;
         SEC08, AT = 439.82295    ;!, SLOT_ID = 2186621;
         SEC09, AT = 502.6548     ;!, SLOT_ID = 2186622;
         SEC00, AT = 565.48665    ;!, SLOT_ID = 2186623;
        ENDSEQUENCE;

        return;

        ! TODO: remove description
        !++END_SEQUENCE++



??? "MAD-X sequence of main units - [direct download](../../../ps_mu.seq)"
        /**********************************************************************************
        * PLACEHOLDERS: 
        * NOTE: reference to CDS note to be written to summarize changes
        * TODO: at each occurrence an action still has to be done
        ************************************************************************************/

        /**********************************************************************************
        *
        * Elements description and sequence file for each PS main unit (MU).
        *
        * Summary of changes with respect to previous versions available at NOTE
        *
        * 11/06/2019 - Alexander Huschauer
        ************************************************************************************/


        /************************************************************************************
        *
        *         DEFINITION OF FOCUSING AND DEFOCUSING HALF-UNITS OF THE MU               
        *
        *************************************************************************************/

        /************************************************************************************
        *        							 F HALF-UNITS     					            
        *************************************************************************************/

        LF   = +2.1260;				! iron length of F half-unit
        DLF := +0.0715925;          ! theoretical bending length correction; value has been rounded on drawing PS_LM___0013 (MU01 assembly) to 0.0716 m
        L_F = LF + DLF;				! total magnetic length

        ! yoke inside
        ANGLE_F := 0.03135884818;  	! angle calculated according to EQ.? in NOTE
        K1_F := +0.05872278;		! TODO: quadrupole gradient to be rematched for the bare machine
        K2_F :=  0.0;				! to be potentially used instead of allocating the PFW sextupole to multipoles

        /************************************************************************************
        *        							 D HALF-UNITS     					            
        *************************************************************************************/

        LD   = +2.1340;          	! iron length of D half-unit
        DLD := +0.0715925;          ! theoretical bending length correction; value has been rounded on drawing PS_LM___0013 (MU01 assembly) to 0.0716 m
        L_D = LD + DLD;				! total magnetic length

        ! yoke inside
        ANGLE_D := 0.03147300489;  	! angle calculated according to EQ.? in (CDS NOTE)
        K1_D := -0.05872278;		! TODO: quadrupole gradient to be rematched for the bare machine
        K2_D :=  0.0;				! to be potentially used instead of allocating the PFW sextupole to multipoles

        /************************************************************************************
        *
        *        MULTIPOLES INSIDE THE MAIN UNITS REPRESENTING THE POLE FACE WINDINGS               
        *		 (TODO: explanation for new multipole description to be added in NOTE)
        *
        *************************************************************************************/

        ! TODO: discuss whether inside or outside yoke description should still be retained
        ! ideally, information from the magnetic model to be incorporated here
        ! TODO: explain disappearance of the junction, being replaced by only a MULTIPOLE

        MP_F: MULTIPOLE, knl := {0, 0, MPK2, MPK3_F, MPK4_F, MPK5_F};
        MP_J: MULTIPOLE, knl := {0, 0, MPK2_J, 0, MPK4_J, MPK5_J};
        MP_D: MULTIPOLE, knl := {0, 0, MPK2, MPK3_D, MPK4_D, MPK5_D};

        /************************************************************************************
        *
        *     DEFINITION OF HORIZONTAL ORBIT CORRECTORS REPRESENTING THE BACKLEG WINDINGS               
        *
        *************************************************************************************/

        ! In reality each DHZ corresponds to a cable around the yoke of two adjacent MUs. 
        ! For example, PR.DHZXX provides a correction along MU(XX-1) and MUXX.
        ! In this model, the effect of each PR.DHZXX is represented by kicks at the location 
        ! of the juntion of MU(XX-1) and MUXX.

        DHZ  : HKICKER  , L := 0;

        /************************************************************************************
        *
        *         						DEFINITION OF EACH MU               
        *
        *************************************************************************************/

        !R          ! D-F unit, yoke outside
        !S          ! F-D unit, yoke outside
        !T          ! F-D unit, yoke inside
        !U          ! D-F unit, yoke inside

        MU_L = L_F + L_D;		! Total magnetic length of one MU
        PR.BH.F: SBEND, L = L_F, ANGLE := ANGLE_F, K1 := K1_F, K2 := K2_F;
        PR.BH.D: SBEND, L = L_D, ANGLE := ANGLE_D, K1 := K1_D, K2 := K2_D;

        PR.BHT01: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ01.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHU02: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ03.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT03: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ03.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR04: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ05.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT05: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ05.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR06: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ07.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHS07: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ07.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR08: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ09.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT09: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ09.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR10: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ11.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHS11: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ11.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR12: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ13.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHS13: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ13.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHU14: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ15.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT15: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ15.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHU16: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ17.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT17: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ17.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHU18: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ19.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHS19: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ19.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR20: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ21.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT21: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ21.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR22: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ23.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT23: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ23.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHU24: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ25.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT25: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ25.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR26: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ27.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHS27: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ27.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHU28: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ29.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT29: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ29.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR30: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ31.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT31: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ31.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR32: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ33.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHS33: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ33.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR34: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ35.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT35: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ35.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR36: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ37.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT37: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ37.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR38: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ39.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT39: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ39.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHU40: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ41.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT41: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ41.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR42: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ43.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT43: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ43.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR44: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ45.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT45: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ45.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR46: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ47.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHS47: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ47.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR48: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ49.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT49: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ49.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR50: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ51.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT51: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ51.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR52: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ53.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHS53: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ53.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR54: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ55.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT55: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ55.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHU56: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ57.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT57: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ57.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHU58: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ59.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT59: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ59.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHU60: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ61.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT61: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ61.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHU62: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ63.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT63: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ63.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHU64: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ65.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT65: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ65.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR66: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ67.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHS67: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ67.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHU68: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ69.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT69: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ69.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR70: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ71.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT71: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ71.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR72: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ73.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHS73: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ73.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHU74: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ75.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT75: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ75.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR76: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ77.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT77: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ77.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR78: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ79.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHS79: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ79.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR80: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ81.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT81: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ81.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR82: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ83.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHS83: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ83.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR84: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ85.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT85: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ85.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR86: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ87.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHS87: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ87.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHU88: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ89.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT89: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ89.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR90: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ91.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT91: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ91.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR92: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ93.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHS93: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ93.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR94: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ95.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT95: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ95.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR96: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ97.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHT97: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ97.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR98: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ99.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHS99: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_F,    AT = 0.0;
         PR.BH.F, AT = L_F/2;
         MP_J,    AT = L_F;
         PR.DHZ99.B: DHZ,  AT = L_F;
         PR.BH.D, AT = L_F + L_D/2;
         MP_D,    AT = MU_L;
        ENDSEQUENCE;

        PR.BHR00: SEQUENCE, refer = CENTRE,  L = MU_L;
         MP_D,    AT = 0.0;
         PR.BH.D, AT = L_D/2;
         MP_J,    AT = L_D;
         PR.DHZ01.A: DHZ,  AT = L_D;
         PR.BH.F, AT = L_D + L_F/2;
         MP_F,    AT = MU_L;
        ENDSEQUENCE;


??? "MAD-X strength definition - [direct download](../../../ps.str)"
        /*******************************************************************************
        **                        Low-energy quadrupoles                              **
        *******************************************************************************/
        !focussing

           PR.QFN05      , K1  :=  KQFN05;
           PR.QFN09      , K1  :=  KQFN09;
           PR.QFW17      , K1  :=  KQFW17;
           PR.QFN21      , K1  :=  KQFN21;
           PR.QFW27      , K1  :=  KQFW27;
           PR.QFW31      , K1  :=  KQFW31;
           PR.QFN35      , K1  :=  KQFN35;
           PR.QFN39      , K1  :=  KQFN39;
           PR.QFN45      , K1  :=  KQFN45;
           PR.QFN49      , K1  :=  KQFN49;
           PR.QFN55      , K1  :=  KQFN55;
           PR.QFW59      , K1  :=  KQFW59;
           PR.QFN67      , K1  :=  KQFN67;
           PR.QFN71      , K1  :=  KQFN71;
           PR.QFN77      , K1  :=  KQFN77;
           PR.QFN81      , K1  :=  KQFN81;
           PR.QFN85      , K1  :=  KQFN85;
           PR.QFN89      , K1  :=  KQFN89;
           PR.QFN95      , K1  :=  KQFN95;
           PR.QFN99      , K1  :=  KQFN99;


           KQFN05 : = kf;
           KQFN09 : = kf;
           KQFW17 : = kf;
           KQFN21 : = kf;
           KQFW27 : = kf;
           KQFW31 : = kf;
           KQFN35 : = kf;
           KQFN39 : = kf;
           KQFN45 : = kf;
           KQFN49 : = kf;
           KQFN55 : = kf;
           KQFW59 : = kf;
           KQFN67 : = kf;
           KQFN71 : = kf;
           KQFN77 : = kf;
           KQFN81 : = kf;
           KQFN85 : = kf;
           KQFN89 : = kf;
           KQFN95 : = kf;
           KQFN99 : = kf;

        !defocussing

           PR.QDW06      , K1  :=  KQDW06;
           PR.QDN10      , K1  :=  KQDN10;
           PR.QDW18      , K1  :=  KQDW18;
           PR.QDW22      , K1  :=  KQDW22;
           PR.QDW28      , K1  :=  KQDW28;
           PR.QDW32      , K1  :=  KQDW32;
           PR.QDN36      , K1  :=  KQDN36;
           PR.QDN40      , K1  :=  KQDN40;
           PR.QDN46      , K1  :=  KQDN46;
           PR.QDN50      , K1  :=  KQDN50;
           PR.QDW56      , K1  :=  KQDW56;
           PR.QDW60      , K1  :=  KQDW60;
           PR.QDN68      , K1  :=  KQDN68;
           PR.QDN72      , K1  :=  KQDN72;
           PR.QDN78      , K1  :=  KQDN78;
           PR.QDN82      , K1  :=  KQDN82;
           PR.QDN86      , K1  :=  KQDN86;
           PR.QDN90      , K1  :=  KQDN90;
           PR.QDN96      , K1  :=  KQDN96;
           PR.QDN00      , K1  :=  KQDN00;


           KQDW06 : = kd;
           KQDN10 : = kd;
           KQDW18 : = kd;
           KQDW22 : = kd;
           KQDW28 : = kd;
           KQDW32 : = kd;
           KQDN36 : = kd;
           KQDN40 : = kd;
           KQDN46 : = kd;
           KQDN50 : = kd;
           KQDW56 : = kd;
           KQDW60 : = kd;
           KQDN68 : = kd;
           KQDN72 : = kd;
           KQDN78 : = kd;
           KQDN82 : = kd;
           KQDN86 : = kd;
           KQDN90 : = kd;
           KQDN96 : = kd;
           KQDN00 : = kd;


        /*******************************************************************************
        **                        Skew quadrupoles                                    **
        *******************************************************************************/
        !focussing
           
           PR.QSK03      , KSL  :=  {0, KQSK03};
           PR.QSK07      , KSL  :=  {0, KQSK07};
           PR.QSK19      , KSL  :=  {0, KQSK19};
           PR.QSK23      , KSL  :=  {0, KQSK23};
           PR.QSK29      , KSL  :=  {0, KQSK29};
           PR.QSK33      , KSL  :=  {0, KQSK33};
           PR.QSK37      , KSL  :=  {0, KQSK37};
           PR.QSK41      , KSL  :=  {0, KQSK41};
           PR.QSK43      , KSL  :=  {0, KQSK43};
           PR.QSK47      , KSL  :=  {0, KQSK47};
           PR.QSK53      , KSL  :=  {0, KQSK53};
           PR.QSK57      , KSL  :=  {0, KQSK57};
           PR.QSK69      , KSL  :=  {0, KQSK69};
           PR.QSK73      , KSL  :=  {0, KQSK73};
           PR.QSK79      , KSL  :=  {0, KQSK79};
           PR.QSK83      , KSL  :=  {0, KQSK83};
           PR.QSK87      , KSL  :=  {0, KQSK87};
           PR.QSK91      , KSL  :=  {0, KQSK91};
           PR.QSK93      , KSL  :=  {0, KQSK93};
           PR.QSK97      , KSL  :=  {0, KQSK97};


        !defocussing

           PR.QSK04      , KSL  :=  {0, KQSK04};
           PR.QSK08      , KSL  :=  {0, KQSK08};
           PR.QSK20      , KSL  :=  {0, KQSK20};
           PR.QSK24      , KSL  :=  {0, KQSK24};
           PR.QSK30      , KSL  :=  {0, KQSK30};
           PR.QSK34      , KSL  :=  {0, KQSK34};
           PR.QSK38      , KSL  :=  {0, KQSK38};
           PR.QSK42      , KSL  :=  {0, KQSK42};
           PR.QSK44      , KSL  :=  {0, KQSK44};
           PR.QSK48      , KSL  :=  {0, KQSK48};
           PR.QSK54      , KSL  :=  {0, KQSK54};
           PR.QSK58      , KSL  :=  {0, KQSK58};
           PR.QSK70      , KSL  :=  {0, KQSK70};
           PR.QSK74      , KSL  :=  {0, KQSK74};
           PR.QSK80      , KSL  :=  {0, KQSK80};
           PR.QSK84      , KSL  :=  {0, KQSK84};
           PR.QSK88      , KSL  :=  {0, KQSK88};
           PR.QSK92      , KSL  :=  {0, KQSK92};
           PR.QSK94      , KSL  :=  {0, KQSK94};
           PR.QSK98      , KSL  :=  {0, KQSK98};

        /*******************************************************************************
        **                  Horizontal correctors (backleg windings)                  **
        *******************************************************************************/

        PR.DHZ01.A, KICK := KDHZ01;
        PR.DHZ01.B, KICK := KDHZ01;
        PR.DHZ03.A, KICK := KDHZ03;
        PR.DHZ03.B, KICK := KDHZ03;
        PR.DHZ05.A, KICK := KDHZ05;
        PR.DHZ05.B, KICK := KDHZ05;
        PR.DHZ07.A, KICK := KDHZ07;
        PR.DHZ07.B, KICK := KDHZ07;
        PR.DHZ09.A, KICK := KDHZ09;
        PR.DHZ09.B, KICK := KDHZ09;
        PR.DHZ11.A, KICK := KDHZ11;
        PR.DHZ11.B, KICK := KDHZ11;
        PR.DHZ13.A, KICK := KDHZ13;
        PR.DHZ13.B, KICK := KDHZ13;
        PR.DHZ15.A, KICK := KDHZ15;
        PR.DHZ15.B, KICK := KDHZ15;
        PR.DHZ17.A, KICK := KDHZ17;
        PR.DHZ17.B, KICK := KDHZ17;
        PR.DHZ19.A, KICK := KDHZ19;
        PR.DHZ19.B, KICK := KDHZ19;
        PR.DHZ21.A, KICK := KDHZ21;
        PR.DHZ21.B, KICK := KDHZ21;
        PR.DHZ23.A, KICK := KDHZ23;
        PR.DHZ23.B, KICK := KDHZ23;
        PR.DHZ25.A, KICK := KDHZ25;
        PR.DHZ25.B, KICK := KDHZ25;
        PR.DHZ27.A, KICK := KDHZ27;
        PR.DHZ27.B, KICK := KDHZ27;
        PR.DHZ29.A, KICK := KDHZ29;
        PR.DHZ29.B, KICK := KDHZ29;
        PR.DHZ31.A, KICK := KDHZ31;
        PR.DHZ31.B, KICK := KDHZ31;
        PR.DHZ33.A, KICK := KDHZ33;
        PR.DHZ33.B, KICK := KDHZ33;
        PR.DHZ35.A, KICK := KDHZ35;
        PR.DHZ35.B, KICK := KDHZ35;
        PR.DHZ37.A, KICK := KDHZ37;
        PR.DHZ37.B, KICK := KDHZ37;
        PR.DHZ39.A, KICK := KDHZ39;
        PR.DHZ39.B, KICK := KDHZ39;
        PR.DHZ41.A, KICK := KDHZ41;
        PR.DHZ41.B, KICK := KDHZ41;
        PR.DHZ43.A, KICK := KDHZ43;
        PR.DHZ43.B, KICK := KDHZ43;
        PR.DHZ45.A, KICK := KDHZ45;
        PR.DHZ45.B, KICK := KDHZ45;
        PR.DHZ47.A, KICK := KDHZ47;
        PR.DHZ47.B, KICK := KDHZ47;
        PR.DHZ49.A, KICK := KDHZ49;
        PR.DHZ49.B, KICK := KDHZ49;
        PR.DHZ51.A, KICK := KDHZ51;
        PR.DHZ51.B, KICK := KDHZ51;
        PR.DHZ53.A, KICK := KDHZ53;
        PR.DHZ53.B, KICK := KDHZ53;
        PR.DHZ55.A, KICK := KDHZ55;
        PR.DHZ55.B, KICK := KDHZ55;
        PR.DHZ57.A, KICK := KDHZ57;
        PR.DHZ57.B, KICK := KDHZ57;
        PR.DHZ59.A, KICK := KDHZ59;
        PR.DHZ59.B, KICK := KDHZ59;
        PR.DHZ61.A, KICK := KDHZ61;
        PR.DHZ61.B, KICK := KDHZ61;
        PR.DHZ63.A, KICK := KDHZ63;
        PR.DHZ63.B, KICK := KDHZ63;
        PR.DHZ65.A, KICK := KDHZ65;
        PR.DHZ65.B, KICK := KDHZ65;
        PR.DHZ67.A, KICK := KDHZ67;
        PR.DHZ67.B, KICK := KDHZ67;
        PR.DHZ69.A, KICK := KDHZ69;
        PR.DHZ69.B, KICK := KDHZ69;
        PR.DHZ71.A, KICK := KDHZ71;
        PR.DHZ71.B, KICK := KDHZ71;
        PR.DHZ73.A, KICK := KDHZ73;
        PR.DHZ73.B, KICK := KDHZ73;
        PR.DHZ75.A, KICK := KDHZ75;
        PR.DHZ75.B, KICK := KDHZ75;
        PR.DHZ77.A, KICK := KDHZ77;
        PR.DHZ77.B, KICK := KDHZ77;
        PR.DHZ79.A, KICK := KDHZ79;
        PR.DHZ79.B, KICK := KDHZ79;
        PR.DHZ81.A, KICK := KDHZ81;
        PR.DHZ81.B, KICK := KDHZ81;
        PR.DHZ83.A, KICK := KDHZ83;
        PR.DHZ83.B, KICK := KDHZ83;
        PR.DHZ85.A, KICK := KDHZ85;
        PR.DHZ85.B, KICK := KDHZ85;
        PR.DHZ87.A, KICK := KDHZ87;
        PR.DHZ87.B, KICK := KDHZ87;
        PR.DHZ89.A, KICK := KDHZ89;
        PR.DHZ89.B, KICK := KDHZ89;
        PR.DHZ91.A, KICK := KDHZ91;
        PR.DHZ91.B, KICK := KDHZ91;
        PR.DHZ93.A, KICK := KDHZ93;
        PR.DHZ93.B, KICK := KDHZ93;
        PR.DHZ95.A, KICK := KDHZ95;
        PR.DHZ95.B, KICK := KDHZ95;
        PR.DHZ97.A, KICK := KDHZ97;
        PR.DHZ97.B, KICK := KDHZ97;
        PR.DHZ99.A, KICK := KDHZ99;
        PR.DHZ99.B, KICK := KDHZ99;

        /*******************************************************************************
        **                        Vertical correctors                                 **
        *******************************************************************************/

        /*
           PR.DVT04      , KICK :=  KDVT04;
           PR.DVT08      , KICK :=  KDVT08;
           PR.DVT12      , KICK :=  KDVT12;
           PR.DVT20      , KICK :=  KDVT20;
           PR.DVT22      , KICK :=  KDVT22;
           PR.DVT24      , KICK :=  KDVT22;
           PR.DVT30      , KICK :=  KDVT22;
           PR.DVT34      , KICK :=  KDVT34;
           PR.DVT38      , KICK :=  KDVT38;
           PR.DVT44      , KICK :=  KDVT44;
           PR.DVT54      , KICK :=  KDVT54;
           PR.DVT64      , KICK :=  KDVT64;
           PR.DVT70      , KICK :=  KDVT70;
           PR.DVT74      , KICK :=  KDVT74;
           PR.DVT76      , KICK :=  KDVT76;
           PR.DVT80      , KICK :=  KDVT80;
           PR.DVT88      , KICK :=  KDVT88;
           PR.DVT94      , KICK :=  KDVT94;
           PR.DVT98      , KICK :=  KDVT98;
        */
        /*******************************************************************************
        **                        Transition quadrupoles                              **
        *******************************************************************************/

        CC406 := (1099.7E-6/0.20) /BRHO;
        CC407 := (3043.E-6/0.20)  /BRHO;
        CC408 := (1000.E-6/0.20)  /BRHO;
        CC409 := (640.E-5/0.30)   /BRHO;

        !Triplets

           PR.QTRTB07    , K1   := +ITRIPB*CC409;
           PR.QTRTA41    , K1   := -ITRIPA*CC407;
           PR.QTRTA49    , K1   := +ITRIPA*CC409;
           PR.QTRTA73    , K1   := -ITRIPA*CC407;
           PR.QTRTB99.A  , K1   := -ITRIPB*CC407;
           PR.QTRTB99.B  , K1   := -ITRIPB*CC407;


        !Doublets

           PR.QTRDA19    , K1   := +IDOUBA*CC406;
           PR.QTRDA27    , K1   := -IDOUBA*CC406;
           PR.QTRDB29    , K1   := -IDOUBB*CC406;
           PR.QTRDB37    , K1   := +IDOUBB*CC408;
           PR.QTRDB61    , K1   := +IDOUBB*CC406;
           PR.QTRDB69    , K1   := -IDOUBB*CC408;
           PR.QTRDA87    , K1   := -IDOUBA*CC408;
           PR.QTRDA95    , K1   := +IDOUBA*CC408;

        /*******************************************************************************
        **                        Injection dipoles                                  **
        *******************************************************************************/

           PI.BSW26.22   , KICK := +BSW26;
           PI.BSW26.30   , KICK := +BSW26;

           PI.BSW40      , KICK := +BSW40;
           PI.BSW42      , KICK := +BSW42;
           PI.BSW43      , KICK := +BSW43;
           PI.BSW44      , KICK := +BSW44;

        /*******************************************************************************
        **                        Extraction dipoles                                  **
        *******************************************************************************/

           PE.BSW12   , KICK := +BSW12;
           PE.BSW14   , KICK := +BSW14;
           PE.BSW20   , KICK := +BSW20;
           PE.BSW22   , KICK := +BSW22;

        /*
           PE.BSW23.19   , KICK := -BSW23* CC205;
           PE.BSW23.27   , KICK := -BSW23*CC205;

           PE.BSW31.27   , KICK := +BSW31a*CC205;
           PE.BSW31.35   , KICK := +BSW31b*CC210;

           PE.BSW57.53   , KICK := -BSW57*CC206/2.0; ! Half kick due to modif on magnet. why?
           PE.BSW57.59   , KICK := +BSW57*CC205/2; ! Half kick due to modif on magnet. Ray doesnt know what.
           PE.BSW57.61   , KICK := -BSW57 * CC213;
           PE.BSW57.67   , KICK := +BSW57*CC206/2; ! Half kick due to modif on magnet. Ray doesnt know what.
        */
        /*******************************************************************************
        **                        High-energy corrector dipole                        **
        *******************************************************************************/
        /*
           PR.DHZOC05    , KICK := +BSW16f * CC210;
           PR.DHZOC18    , KICK := +BSW16e*CC205;
           PR.DHZOC60    , KICK := +DHZ60 * CC206;
        */
        /*******************************************************************************
        **                               MTE elements                                 **
        *******************************************************************************/

        !sextupoles

           PR.XNO39.A    , K2 :=  KXNO39;
           PR.XNO39.B    , K2 :=  KXNO39;
           PR.XNO55.A    , K2 :=  KXNO55;
           PR.XNO55.B    , K2 :=  KXNO55;

        !octupoles

           PR.ONO39      , K3  :=  KONO39;
           PR.ONO55      , K3  :=  KONO39;

           PR.ODN40      , K3  :=  KODN;
           PR.ODN50      , K3  :=  KODN;
           PR.ODN52.A    , K3  :=  KODN;
           PR.ODN52.B    , K3  :=  KODN;
           PR.ODN70.A    , K3  :=  KODN;
           PR.ODN70.B    , K3  :=  KODN;
           PR.ODN90      , K3  :=  KODN;
           PR.ODN00      , K3  :=  KODN;

        /*******************************************************************************
        **                        Extraction kickers                                  **
        *******************************************************************************/

           PE.KFA04      , KICK :=  KKFA04;
           PE.KFA13      , KICK :=  KKFA13;
           PE.KFA21      , KICK :=  KKFA21;
           PE.KFA71      , KICK :=  KKFA71;

        /*******************************************************************************
        **                        Slow extraction elements                            **
        *******************************************************************************/

        ! quadrupoles

           PR.QSE29      , K1   := KQSE;
           PR.QSE87      , K1   := KQSE;

        !sextupoles

           PR.XSE01.A    , K2  :=  KXSE1;
           PR.XSE01.B    , K2  :=  KXSE1;
           PR.XSE07      , K2  :=  KXSE2;

        /*******************************************************************************
        **                                    QKEs                                    **
        *******************************************************************************/

           PE.QKE16.05   , K1   := -KQKE16;
           PE.QKE16.25   , K1   :=  KQKE16;

        /*
           PE.QKE25      , K1   := +QKE162*CC414;
           PE.QKE73      , K1   := -QKE162*CC414;
        */

        /*******************************************************************************
        **                          Vertical sextupoles                               **
        *******************************************************************************/
        /*     
           PR.XNO60      , knl  :=  {0,0,IXNO*CC608};  ! SG 2014 -WARNING - check current name
           PR.XNO94      , knl  :=  {0,0,IXNO*CC608};  ! SG 2014 -WARNING - check current name
        */
        /*******************************************************************************
        **  Resonance compensation sextupoles (magnet with normal and skew circuits)  **
        *******************************************************************************/
        /*   
           PR.XSK10      ,  KNL:= {0.0, 0.0 ,0.108*IXcomp3/(BRHO)} , KSL:= {0.0, 0.0, 0.09*IXcomp4/(2*BRHO)};
           PR.XSK14      ,  KNL:= {0.0, 0.0 ,0.108*IXcomp3/(BRHO)} , KSL:= {0.0, 0.0, 0.09*IXcomp4/(2*BRHO)};
           PR.XSK52      ,  KNL:= {0.0, 0.0 ,0.108*IXcomp3/(BRHO)} , KSL:= {0.0, 0.0, 0.09*IXcomp4/(2*BRHO)};
           PR.XSK58      ,  KNL:= {0.0, 0.0 ,0.108*IXcomp3/(BRHO)} , KSL:= {0.0, 0.0, 0.09*IXcomp4/(2*BRHO)};
        */
        RETURN;
