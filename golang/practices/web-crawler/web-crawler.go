package main

import (
	"fmt"
	"sync"
)

type Fetcher interface {
	// Fetch returns the body of URL and
	// a slice of URLs found on that page.
	Fetch(url string) (body string, urls []string, err error)
}

// fakeFetcher is Fetcher that returns canned results.
type fakeFetcher map[string]*fakeResult

func (f fakeFetcher) Fetch(url string) (string, []string, error) {
	if res, ok := f[url]; ok {
		return res.body, res.urls, nil
	}
	return "", nil, fmt.Errorf("not found: %s", url)
}

// Crawl uses fetcher to recursively crawl
// pages starting with url, to a maximum of depth.
func Crawl(url string, depth int, fetcher Fetcher, urlMap *SafeMap) {
	//https://stackoverflow.com/questions/13217547/tour-of-go-exercise-10-crawler
	defer wg.Done()

	if depth <= 0 {
		return
	}

	body, urls, err := fetcher.Fetch(url)
	urlMap.Set(url, body)
	if err != nil {
		fmt.Println(err)
		return
	}


	for _, u := range urls {
		if _, ok := urlMap.Value(url); !ok {
			wg.Add(1)
			go Crawl(u, depth-1, fetcher, urlMap)
		}
		
	}

	return
}

type fakeResult struct {
	body string
	urls []string
}

// fetcher is a populated fakeFetcher.
var fetcher = fakeFetcher{
	"https://golang.org/": &fakeResult{
		"The Go Programming Language",
		[]string{
			"https://golang.org/pkg/",
			"https://golang.org/cmd/",
		},
	},
	"https://golang.org/pkg/": &fakeResult{
		"Packages",
		[]string{
			"https://golang.org/",
			"https://golang.org/cmd/",
			"https://golang.org/pkg/fmt/",
			"https://golang.org/pkg/os/",
		},
	},
	"https://golang.org/pkg/fmt/": &fakeResult{
		"Package fmt",
		[]string{
			"https://golang.org/",
			"https://golang.org/pkg/",
		},
	},
	"https://golang.org/pkg/os/": &fakeResult{
		"Package os",
		[]string{
			"https://golang.org/",
			"https://golang.org/pkg/",
		},
	},
}

type SafeMap struct {
	m map[string]string
	mux sync.Mutex
}

func (v *SafeMap) Value(key string) (string, bool) {
	v.mux.Lock()
	defer v.mux.Unlock()
	val, ok := v.m["key"]
	return val, ok
}

func (v *SafeMap) Set(key string, value string) {
	v.mux.Lock()
	v.m[key] = value
	v.mux.Unlock()
}

var wg sync.WaitGroup

func main() {
	urlMap := SafeMap{m: make(map[string]string)}

	wg.Add(1)
	go Crawl("https://golang.org/", 4, fetcher, &urlMap)
	wg.Wait()

	for url := range urlMap.m {
		body, _ := urlMap.Value(url)
		fmt.Printf("found: %s %q\n", url, body)
	}
}
