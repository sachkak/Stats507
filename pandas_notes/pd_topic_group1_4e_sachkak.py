# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     notebook_metadata_filter: markdown
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.12.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# ## Topics in Pandas
# **Stats 507, Fall 2021** 
#   

# ## Contents
#
# + [Function](Function) 
# + [Topic 2 Title](#Topic-2-Title)

# ## Function
# Defining parts of a Function
#
# **Sachie Kakehi**
#
# sachkak@umich.edu


# ## What is a Function
#
#   - A *function* is a block of code which only runs when it is called.
#   - You can pass data, known as *parameters* or *arguments*, into a function.
#   - A function can return data as a result.

# ## Parts of a Function
#
#   - A function is defined using the $def$ keyword
#   - Parameters or arguments are specified after the function name, inside the parentheses.
#   - Within the function, the block of code is defined, often $print$ or $return$ values.

# ## Example
#
#   - The following function multiplies the parameter, x, by 5:
#   - Note : it is good practice to add a docstring explaining what the function does, and what the parameters and returns are. 

def my_function(x):
    """
    The function multiplies the parameter by 5.
    
    Parameters
    ----------
    x : A float or integer.
    
    Returns
    -------
    A float or integer multiplied by 5. 
    """
    return 5 * x
print(my_function(3))


