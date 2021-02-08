import copy

# a sentence in conjunctive normal form is made up of a conjunction of clauses which in turn are made up of a disjunction of propositions

def get_propositions(sentence):
    propositions = []
    for clause in sentence:
        for proposition in clause:
            propositions.append(proposition)
            if len(proposition) == 1:
                negation = '-' + proposition
                propositions.append(negation)
            else:
                negation = proposition[-1]
                propositions.append(negation)
    propositions = list(set(propositions))
    return propositions

def create_initial_model(propositions):
    model = {}
    for proposition in propositions:
        model[proposition] = None
    return model

def DPLL_satisfiable(sentence):
    propositions = get_propositions(sentence)
    model = create_initial_model(propositions)
    frontier = [model]
    while len(frontier) > 0:
        result = DPLL(sentence, propositions, frontier)
        if result:
            print("satisfiable:")
            print(result)
            return result
    print("not satisfiable")

def evaluate_clause(clause, model):
    false_count = 0
    for proposition in clause:
        if model[proposition] == True:
            return True
        if model[proposition] == False:
            false_count += 1
    if false_count == len(clause):
        return False
    return None

def check_statisfiable(sentence, model):
    true_count = 0
    for clause in sentence:
        if evaluate_clause(clause, model) == False:
            return False
        if evaluate_clause(clause, model) == True:
            true_count += 1
    if true_count == len(sentence):
        return True
    return None

def handle_pure_propositions(sentence, model):
    pure_propositions = find_pure_symbols(sentence, model)
    for proposition in pure_propositions:
        model[proposition] = True
        if len(proposition) == 2:
            model[proposition[-1]] = False
        else:
            model['-' + proposition] = False
    return model

def no_negation_contradictions(model):
    for key in model.keys():
        if model[key] != None:
            if len(key) == 2:
                if model[key[-1]] == model[key]:
                    return False
            if len(key) == 1:
                if model['-' + key] == model[key]:
                    return False
    return True

def fill_negations(model):
    for key in model.keys():
        if model[key] == True:
            if len(key) == 2:
                model[key[-1]] = False
            if len(key) == 1:
                model['-' + key] = False
        if model[key] == False:
            if len(key) == 2:
                model[key[-1]] = True
            if len(key) == 1:
                model['-' + key] = True

def handle_unit_propositions(sentence, model):
    new_sentence = []
    for clause in sentence:
        if evaluate_clause == None:
            new_clause = []
            for proposition in sentence:
                if model[proposition] == None:
                    new_clause.append(proposition)
            new_sentence.append(new_clause)
    for clause in new_sentence:
        if len(clause) == 1:
            model[clause[0]] = True
    return model

def DPLL(sentence, propositions, frontier):
    model = frontier.pop()
    model = handle_pure_propositions(sentence, model)
    if no_negation_contradictions(model):
        fill_negations(model)
        handle_unit_propositions(sentence, model)
        if no_negation_contradictions(model):
            fill_negations(model)
            statisfiable = check_statisfiable(sentence, model)
            if statisfiable == True:
                #return the model that satisfies the sentence
                return model
            if statisfiable == None:
                # expand
                for num, key in enumerate(model.keys()):
                    if model[key] == None:
                        model_copy = copy.deepcopy(model)
                        model_copy[key] = True
                        frontier.append(model_copy)
                        model_copy[key] = False
                        frontier.append(model_copy)

def find_pure_symbols(sentence, model):
    propositions = []
    for clause in sentence:
        for proposition in clause:
            if model[proposition] == None:
                propositions.append(proposition)
    impure_propositions = []
    for index1 in range(len(propositions)):
        for index2 in range(len(propositions)):
            if index1 != index2:
                if propositions[index1][-1] == propositions[index2][-1]:
                    impure_propositions.append(propositions[index1])
    pure_propositions = []
    for proposition in propositions:
        if proposition[-1] not in impure_propositions:
            pure_propositions.append(proposition)
    return pure_propositions


#sentence = [['a','b'],['-b','c'],['d','a'],['d','c']]
sentence = [['-c','-d'],['-e','-f'],['-j','-k'],['-g','b'],['-b','h'],['-a','-d','h'],['-g','i'],['-f','i'],['-b','-a'],['-d','-f','k'],['-h','-i','k'], ['a'],['j'],['d']]
#sentence = [['-c','-d'],['-e','-f'],['-j','-k'],['-g','b'],['-b','h'],['-a','-d','h'],['-g','i'],['-f','i'],['-b','-a'],['-d','-f','k'],['-h','-i','k']]
DPLL_satisfiable(sentence)