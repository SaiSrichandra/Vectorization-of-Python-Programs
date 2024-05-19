
import os
from flask import Flask, render_template, request,send_file
import ast
import tree
import variable_classifier
import python_ast_utils
import ast2vec
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import json
from sklearn.decomposition import PCA
from sklearn.mixture import GaussianMixture

import traceback
matplotlib.use('Agg')


app = Flask(__name__)

programs     = ['']
traces       = []
model = None
X = None
tree_index = None
programs_to_trees = None
vc = None
trees = None
totno = 0
flist = []

def func(x):
  return len(str(x))

def load_n_encode():
    global model, trees
    X = ast2vec.encode_trees(model, trees)
    return X

def check_data(rollno):
    if not os.path.exists(f'./mock_dataset/{rollno}'):
        os.mkdir(f'./mock_dataset/{rollno}')
    for f in os.listdir(f'./mock_dataset/{rollno}'):
        os.remove(os.path.join(f'./mock_dataset/{rollno}', f))

def get_trees():
    global programs, traces, programs_to_trees
    student_dirs = list(sorted(os.listdir('mock_dataset')))
    totno = len(student_dirs)
    for student_dir in student_dirs:
        trace = [0]
        steps = list(sorted(os.listdir(f'mock_dataset/{student_dir}')))
        for step in steps:
            with open(f'mock_dataset/{student_dir}/{step}', encoding="utf8") as program_file:
                
                trace.append(len(programs))
                try:
                    programs.append(program_file.read())
                    flist.append(step)
                except:
                    print("File reading Error at -----------" + str(step))
                    
        traces.append(trace)
    print('read %d traces with %d programs' % (len(traces), len(programs)))
    trees, programs_to_trees = python_ast_utils.parse_asts(programs, filter_uniques = True, verbose=True, flist = flist)
    import pickle
    file_name = "tree_list_1.pkl"
    open_file = open(file_name,"wb")
    sorted_trees = sorted(trees, key=func)
    print("Sorted with min len = ", str(func(trees[0]))," max len = ", str(func(trees[-1])))
    pickle.dump(sorted_trees, open_file)
    print("Pickled ", len(trees), "unique syntax trees")
    for pk in sorted_trees:
        print(str(func(pk)), end = "   ")
    return trees

def print_ast(filename):
    with open(filename) as f:
        return (ast.dump(ast.parse(f.read())))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download')
def downloadFile ():
    path = os.getcwd()+"/student_ide/app.exe"
    return send_file(path, as_attachment=True)
    
@app.route('/student', methods=['POST', 'GET'])
def student_page():
    try:
        if request.method == "POST":
            if len(request.files.getlist('files[]'))!=0:
                files = request.files.getlist('files[]')
                for file in files:
                    filename = file.filename
                    rollno, stepno, prgno = filename.split('-')
                    check_data(rollno)
                for file in files:
                    filename = file.filename
                    rollno, stepno, prgno = filename.split('-')
                    new_name = f"./mock_dataset/{rollno}/"+f"step_{stepno}.txt"
                    file.save(new_name)

            else:
                files = dict(request.files)
                # file_name = rollno-traceno-prgno.txt
                for _,file in files.items():
                    filename = file.filename
                    rollno, stepno, prgno = filename.split('-')
                    check_data(rollno)
                for _,file in files.items():
                    filename = file.filename
                    rollno, stepno, prgno = filename.split('-')
                    if not os.path.exists(f'./mock_dataset/{rollno}'):
                        os.mkdir(f'./mock_dataset/{rollno}')
                    new_name = f"./mock_dataset/{rollno}/"+f"step_{stepno}.txt"
                    file.save(new_name)
                    
            return '<h1> Successful Upload </h1>'
        else:
            return  render_template('student_page.html')

    except Exception as e:
        return render_template("err.html", error = e)  
		
@app.route('/educator')
def educator_page():
    global X, trees
    trees = get_trees()
    X = load_n_encode()
    return render_template('educator_page.html')

@app.route('/dashboard')
def dashboard_details():
    student_dirs = list(sorted(os.listdir('mock_dataset')))
    totno = len(student_dirs)
    return render_template('educator_page_old.html', tot_no = totno)


# @app.route('/performance_details')
def handle_educator_request():
    
    global traces, tree_index, programs_to_trees, vc, model, trees, X
    # get the index of the program, which is the last program in the first trace
    program_index = traces[0][-1]
    # get the corresponding syntax tree index
    tree_index = programs_to_trees[program_index]

    vc = variable_classifier.VariableClassifier(model)
    vc.fit(trees);
    # try:
    #     plt.figure(figsize = (15, 10))
    #     ast2vec.interpolation_plot(model, start_tree = 0, target_tree = tree_index, X = X, variable_classifier = vc)
    #     plt.savefig('./static/images/intr_plt.png')
    #     plt.clf()

    #     tree_traces = [[0] + [programs_to_trees[program] for program in trace] for trace in traces]
    #     ast2vec.traces_plot(start = 0, target = tree_index, traces = tree_traces, X = X, trees = trees, plot_code = 3)
    #     plt.savefig('./static/images/trace_plt.png')
    #     plt.clf()

    #     W = ast2vec.construct_dynamical_system(tree_index, X, tree_traces)
    #     ast2vec.dynamical_system_plot(W, start_tree = 0, target_tree = tree_index, X = X, arrow_scale = 2., model = model, variable_classifier = vc)

    #     plt.savefig('./static/images/dynamic_plt.png')
    #     plt.clf()
    #     # return render_template('performance_details.html', graphJSON=graphJSON)
    #     return render_template('untitled1.html', name = 'new_plot', url ='/static/images/test.png')
    # except Exception as e:
    #     print('Error Occured')
    #     return str(traceback.print_exc())
    
@app.route('/interpolation_plot')
def interpolation_plot():
    global traces, tree_index, programs_to_trees, vc, model, trees, X
    if vc is None: 
        handle_educator_request()
    plt.figure(figsize = (15, 10))
    ast2vec.interpolation_plot(model, start_tree = 0, target_tree = tree_index, X = X, variable_classifier = vc)
    plt.savefig('./static/images/intr_plt.png')
    plt.clf()
    return render_template('intr.html')
    
@app.route('/trace_plot')
def trace_plot():
    global traces, tree_index, programs_to_trees, vc, model, trees, X
    if vc is None: 
        handle_educator_request()
    tree_traces = [[0] + [programs_to_trees[program] for program in trace] for trace in traces]
    ast2vec.traces_plot(start = 0, target = tree_index, traces = tree_traces, X = X, trees = trees, plot_code = 3)
    plt.savefig('./static/images/trace_plt.png')
    plt.clf()
    return render_template('trace.html')


@app.route('/dynamic_plot')
def dynamic_plot():
    global traces, tree_index, programs_to_trees, vc, model, trees, X
    if vc is None: 
        handle_educator_request()
    tree_traces = [[0] + [programs_to_trees[program] for program in trace] for trace in traces]
    W = ast2vec.construct_dynamical_system(tree_index, X, tree_traces)
    ast2vec.dynamical_system_plot(W, start_tree = 0, target_tree = tree_index, X = X, arrow_scale = 2., model = model, variable_classifier = vc)
    plt.savefig('./static/images/dynamic_plt.png')
    plt.clf()
    return render_template('dynamic.html')

@app.route('/clus_plot')
def clus_plot():
    global traces, tree_index, programs_to_trees, vc, model, trees, X
    if vc is None: 
        handle_educator_request()

    dimred = PCA(n_components = 5)
    Xlo = dimred.fit_transform(X)
    print('our PCA model retains %g percent of the variance' % (100 * np.sum(dimred.explained_variance_ratio_)))

    n_clusters = 4
    clust = GaussianMixture(n_components = n_clusters, covariance_type = 'diag')
    Y = clust.fit_predict(Xlo)
    # extract the cluster means and map them back to the high-dimensional space
    means = dimred.inverse_transform(clust.means_)
    plt.figure(figsize = (15, 10))
    ast2vec.cluster_plot(start = 0, target = tree_index, X = X, Y = Y, means = means, model = model, variable_classifier = vc)
    plt.savefig('./static/images/clus_plt.png')
    plt.clf()
    return render_template('clust.html')


if __name__ == '__main__':

    model = ast2vec.load_model()
    print('Model is loaded!')
    app.run(debug = True, port=5001)