#! python
import rivtlib.rvapi as rv

# rv rv_localB: True

# %% intro
rv.I("""Project description
     Design of embedded pole foundations for a ground mounted photovoltaic array.
     Design is per 2024 IBC Eq 6-1 and Table 18-I-A.
    """)
# %% values
rv.V("""Design input 
     Kyrocera 200GT module data _[T]
     length_mod ==: 56.2*inch |inch, cm, 2 | module length
     width_mod ==: 39.0*inch |inch, cm, 2 | module width
     wt_mod ==: 40.7*lbf | lbf, kN, 2| module weight

     Array dimensions_[T]
     module_tilt ==: 40*rad | rad, rad, 2| module tilt
     spacing ==: 15*ft |ft, m, 2 | post spacing
     gap ==: 18*inch |inch, cm, 2| ground clearance
      
    """)
# %% wind pressure
rv.V("""Design wind pressure
    Exposure B, Risk Category II _[T]
    V ==: 96*mph |mph, mph,1 | Basic wind speed
    K_z ==: 0.57 | 1, 1, 1 | Velocity pressure exposure coefficient
    K_zt ==: 1.0 | 1, 1, 1 | Topography factor
    K_e ==: 1.0 | 1,1,3 | Ground elevastion factor

    ## I added this equation (this is a non-printing comment)
    dummy_1 <=: wt_mod/width_mod | lbf/inch, N/mm, 2 | module weight per unit width _[E]
    """)


# %% tool
rv.S("""Metadata

    _[[PYTHON]] 
    rv_metaD = {
    "authors": "rholland",
    "version": "0.7.1",
    "email": "rod.h.holland@gmail.com",
    "repo": "https://github.com/rivt-info/rivt-single-doc",
    "license": "https://opensource.org/license/mit/",
    "fork1": ["author", "version", "email", "repo"],
    "fork2": [],
    }
    _[[END]]

    """)
# %% doc
rv.S("""Publish Doc 

     _[[METADATA]] 
    [primary]
    authors = rholland
    version = 0.8.1
    repo = https://github.com/rivt-info/rivt-single-doc
    license = https://opensource.org/license/mit/
    [forks]
    fork1 = _author_, _version_, _repo_
    _[[END]]

    _[[LAYOUT]]    
    [general]
    logopath = logo.png
    footer = docname, author, date, time, version
    pagesize = letter
    margins = 1in, 1in, 1in, 1in
    [pdf]
    header = page, totalpages
    stylesheet = rlab.yaml
    cover = cover.rst
    [html]
    cssfile =  htmlsite.css
    [text]
    title = docname, author, date, time, version
    width=80    
    [texpdf]
    header = page, totalpages
    stylesheet = texpdf.sty
    cover = cover.tex
    _[[END]]
    
    | PUBLISH | flagpole test | text

    """)
