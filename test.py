from ir_metrics import f_measure, avg_precision_at_k, dcg, to_relevance_scores,\
    precision_at_k, recall

y_true = list('abcdefg')
y_pred = list('czbajepgard')
rel_scores = to_relevance_scores(y_true, y_pred)
print("rel_scores: {}".format(rel_scores))

print("prec@k: {}".format(precision_at_k(y_true, y_pred)))
print("recalls: {}".format(recall(y_true, y_pred)))
# prec, rec, f1 = f_measure(y_true, y_pred)
# print('precision: {:.4f}'.format(prec))
# print('recall: {:.4f}'.format(rec))
print('f1: {:.4f}'.format(f_measure(y_true, y_pred)))
print('avg_prec at 1: {:.4f}'.format(avg_precision_at_k(y_true, y_pred, k=1)))
print('avg_prec at 3: {:.4f}'.format(avg_precision_at_k(y_true, y_pred, k=3)))
print('avg_prec: {:.4f}'.format(avg_precision_at_k(y_true, y_pred)))
print('dcg: {:.4f}'.format(dcg(y_true, y_pred)))
print('dcg: {:.4f}'.format(dcg([], list('abcdef'))))
print('dcg: {:.4f}'.format(dcg([], list('abcdef'), rel_scores=[3,2,3,0,1,2])))
# print(to_relevance_scores(y_true, y_pred))
