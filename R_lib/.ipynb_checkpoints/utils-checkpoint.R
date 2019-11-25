TokenManager <- function(token_file, copy_from_clipboard=F) {
    if (copy_from_clipboard == T) {
        tryCatch({
            token = read.delim(pipe("pbpaste"),
                               header = F,
                               stringsAsFactors=F)[[1]]
            write(token,
                  file = token_file, append = F)
            print("Token read from clipboard")
        }, warning = function(w) {
            token = read.delim(pipe("pbpaste"),
                               header = F,
                               stringsAsFactors=F)[[1]]
            write(token,
                  file = token_file, append = F)
            print("Token read from clipboard")
        }, error = function(e) {
            print(e)
            print("Couldn't read from clipboard!")
        })
    }
    token = scan(token_file, what = "character")
    return(token)
}