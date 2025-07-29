import os, requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP('serp-images-light')


serp_url = "https://serpapi.com/search"
serp_api_key = os.getenv("SERP_API_KEY")

@mcp.tool()
def search_images_light(q: Annotated[str, Field(description='Parameter defines the query you want to search. You can use anything that you would use in a regular Google Images Light search. e.g. inurl:, site:, intitle:.')],
                        location: Annotated[Union[str, None], Field(description="Parameter defines from where you want the search to originate. If several locations match the location requested, we'll pick the most popular one. Head to the /locations.json API if you need more precise control. The location and uule parameters can't be used together. It is recommended to specify location at the city level in order to simulate a real user’s search. If location is omitted, the search may take on the location of the proxy.")] = None,
                       period_unit: Annotated[Union[str, None], Field(description="Parameter defines the time period unit to search for the recent images, e.g. from past minute, hour, day etc. Options: s - Second, n - Minute, h - Hour, d - Day, w - Week, m - Month, y - Year. This parameter can't be used with start_date/end_date parameters. This parameter overrides qdr component of tbs parameter.")] = None,
                       period_value: Annotated[Union[int, None], Field(description="Parameter defines an optional time period value that can be used with period_unit to describe time periods like 15 seconds, 42 hours, 178 days etc. Default value: 1. Value range: 1..2147483647")] = None,
                       start_date: Annotated[Union[str, None], Field(description="Parameter defines the start date of time period you want to limit the image search to. Format: YYYYMMDD. Example: 20241201. This parameter can't be used with period_unit/period_value parameters. start_date with blank end_date produces date range FROM start_date TO today. This parameter overrides cdr and cd_min components of tbs parameter.")] = None,
                       end_date: Annotated[Union[str, None], Field(description="Parameter defines the end date of time period you want to limit the image search to. Format: YYYYMMDD. Example: 20241231. This parameter can't be used with period_unit/period_value parameters. end_date with blank start_date produces date range BEFORE end_date. This parameter overrides cdr and cd_max components of tbs parameter.")] = None,
                       tbs: Annotated[Union[str, None], Field(description="(to be searched) parameter defines advanced search parameters that aren't possible in the regular query field.")] = None,
                       imgar: Annotated[Union[str, None], Field(description="Parameter defines the set aspect ratio of images. Options: s - Square, t - Tall, w - Wide, xw - Panoramic")] = None,
                       imgsz: Annotated[Union[str, None], Field(description="Parameter defines the size of images. Options: l - Large, m - Medium, i - Icon, qsvga - Larger than 400×300, vga - Larger than 640×480, svga - Larger than 800×600, xga - Larger than 1024×768, 2mp - Larger than 2 MP, 4mp - Larger than 4 MP, 6mp - Larger than 6 MP, 8mp - Larger than 8 MP, 10mp - Larger than 10 MP, 12mp - Larger than 12 MP, 15mp - Larger than 15 MP, 20mp - Larger than 20 MP, 40mp - Larger than 40 MP, 70mp - Larger than 70 MP")] = None,
                       image_color: Annotated[Union[str, None], Field(description="Parameter defines the color of images. Options: bw - Black and white, trans - Transparent, red - Red, orange - Orange, yellow - Yellow, green - Green, teal - Teal, blue - Blue, purple - Purple, pink - Pink, white - White, gray - Gray, black - Black, brown - Brown. This parameter overrides ic and isc components of tbs parameter")] = None,
                       image_type: Annotated[Union[str, None], Field(description="Parameter defines the type of images. Options: face - Face, photo - Photo, clipart - Clip art, lineart - Line drawing, animated - Animated. This parameter overrides itp component of tbs parameter")] = None,
                       licenses: Annotated[Union[str, None], Field(description="Parameter defines the scope of licenses of images. Options: f - Free to use or share, fc - Free to use or share, even commercially, fm - Free to use, share or modify, fmc - Free to use, share or modify, even commercially, cl - Creative Commons licenses, ol - Commercial and other licenses. This parameter overrides sur component of tbs parameter")] = None,
                       safe: Annotated[Union[str, None], Field(description="Parameter defines the level of filtering for adult content. It can be set to active or off, by default Google will blur explicit content.")] = None,
                       nfpr: Annotated[Union[int, None], Field(description="Parameter defines the exclusion of results from an auto-corrected query when the original query is spelled wrong. It can be set to 1 to exclude these results, or 0 to include them (default). Note that this parameter may not prevent Google from returning results for an auto-corrected query if no other results are available.")] = None,
                       filter: Annotated[Union[int, None], Field(description="Parameter defines if the filters for 'Similar Results' and 'Omitted Results' are on or off. It can be set to 1 (default) to enable these filters, or 0 to disable these filters.")] = None,
                       start: Annotated[Union[int, None], Field(description="Parameter defines the result offset. It skips the given number of results. It's used for pagination. (e.g., 0 (default) is the first page of results, 20 is the 2nd page of results, 40 is the 3rd page of results, etc.).")] = None,
                       device: Annotated[Union[str, None], Field(description="Parameter defines the device to use to get the results. It can be set to desktop (default) to use a regular browser, tablet to use a tablet browser (currently using iPads), or mobile to use a mobile browser.")] = None,
                       no_cache: Annotated[Union[bool, None], Field(description="Parameter will force SerpApi to fetch the Google Images Light results even if a cached version is already present. A cache is served only if the query and all parameters are exactly the same. Cache expires after 1h. Cached searches are free, and are not counted towards your searches per month. It can be set to false (default) to allow results from the cache, or true to disallow results from the cache. no_cache and async parameters should not be used together.")] = None,
                       aasync: Annotated[Union[bool, None], Field(description="Parameter defines the way you want to submit your search to SerpApi. It can be set to false (default) to open an HTTP connection and keep it open until you got your search results, or true to just submit your search to SerpApi and retrieve them later. In this case, you'll need to use our Searches Archive API to retrieve your results. async and no_cache parameters should not be used together. async should not be used on accounts with Ludicrous Speed enabled.")] = None,
                       zero_trace: Annotated[Union[bool, None], Field(description="Enterprise only. Parameter enables ZeroTrace mode. It can be set to false (default) or true. Enable this mode to skip storing search parameters, search files, and search metadata on our servers. This may make debugging more difficult.")] = None
            ):
    '''Use this tool to search for images with Google Images Light search engine.'''

    if location:
        q = q + ", location: %s"%location

    payload = {
        'q': q,
        'engine': "google_images_light",
        'api_key': serp_api_key,
        'period_unit': period_unit,
        'period_value': period_value,
        'start_date': start_date,
        'end_date': end_date,
        'tbs': tbs,
        'imgar': imgar,
        'imgsz': imgsz,
        'image_color': image_color,
        'image_type': image_type,
        'licenses': licenses,
        'safe': safe,
        'nfpr': nfpr,
        'filter': filter,
        'start': start,
        'device': device,
        'no_cache': no_cache,
        'async': aasync,
        'zero_trace': zero_trace
    }
    payload = {k: v for k, v in payload.items() if v is not None}

    response = requests.get(serp_url, params=payload)
    print(response)
    return response.json()

if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9999
    mcp.run(transport="stdio")
