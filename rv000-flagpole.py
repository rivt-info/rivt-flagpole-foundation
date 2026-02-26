#! python
import rivtlib.rvapi as rv

# rv rv_localB: True
# rv rv_docname: Flagpole example

# %% intro
rv.I("""Project description
     Design of embedded pole foundations for a ground mounted photovoltaic array.
     Design is per 2024 IBC Eq 6-1 and Table 18-I-A.
    """)
# %% values
rv.V("""Design input 
     Kyrocera 200GT module data _[T]
     length_mod := 56.2*inch |inch, cm, 2 | module length
     width_mod := 39.0*inch |inch, cm, 2 | module width
     wt_mod := 40.7*lbf | lbf, kN, 2| module weight

     Array dimensions_[T]
     module_tilt := 40*deg | deg, rad, 2| module tilt
     spacing := 15*ft |ft, m, 2 | post spacing
     gap := 18*inch |inch, cm, 2| ground clearance
      
    """)
# %% wind pressure
rv.V("""Design wind pressure
     V <= 96*mph |mph, mps,1 | Basic wind speed _[E]
     
     Exposure B, Risk Category II
     K_z := 0.57*1 |1, 1, 1 | Velocity pressure exposure coefficient
     K_zt := 1.0*1 |1, 1, 1 | Topography factor
     K_e := 1.0*1 |1,1,3 | Ground elevastion factor

    """)
# %% force
rv.S("""Force and Stress
        
        m_1 <= omega_1 * S_1**2 / 8 | ftkips, mkN, 2 | mid-span UDL moment _[E]

        fb_1 <= m_1 / section_1 | psi, MPA, 1 | bending stress _[E]
    
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

    _[[LAYOUT]]
        imagepath: 
        pdfheader: ###Page### of ###TotalPages###
        footer: []
    _[[END]]
    
    | PUBLISH | rivt | rst2pdf

    """)
