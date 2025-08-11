from ddgs import DDGS

def get_url(query):
    def search(q):
        with DDGS() as ddgs:
            # Obtener hasta 10 resultados con ddgs.text
            results = list(ddgs.text(q, max_results=10))
            # Extraer solo la URL de cada resultado
            urls = [r['href'] for r in results]
            return urls

    results = search(f"site:youtube.com {query}")
    
    return results[0]
