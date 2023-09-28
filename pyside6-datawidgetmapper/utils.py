from diff_match_patch import diff_match_patch

def create_diff(txn, ytext, current_text, widget_text):
    dmp = diff_match_patch()
    d = dmp.diff_main(current_text, widget_text)
    dmp.diff_cleanupSemanticLossless(d)
    print(d)

