from bs4 import BeautifulSoup

html_content = '''
<li class="mb-12">
    <a aria-current="page" href="/fr-fr/p/go/da1c1e63-879b-4bef-b43a-4760328ac174#l=12&amp;mobilePlanOfferId=753011e4-3eb1-4b87-9ef8-117a5e066371&amp;scroll=false" class="router-link-active router-link-exact-active focus-visible-outline-default-hi rounded-sm relative flex size-full flex-col border py-12 no-underline bg-surface-brand-hi border-action-default-low-pressed hover:bg-surface-brand-hi hover:border-action-default-low-pressed" rel="nofollow noreferrer noopener" aria-disabled="false" disabled="false">
        <div class="m-auto flex w-full flex-row items-center pl-8 pr-16">
            <div class="shrink-0" data-test="icon">
                <div aria-hidden="" class="flex size-[24px] items-center justify-center">
                    <div class="rounded-full border bg-action-default-hi border-action-default-hi" style="width: 8px; height: 8px;"></div>
                </div>
            </div>
            <div class="ml-16 flex grow flex-col">
                <div class="flex grow flex-row items-baseline text-left">
                    <span class="grow text-action-default-hi body-1-bold">État correct</span>
                </div>
                <div class="body-2 shrink-0 pt-4 text-left text-action-default-low">869,00&nbsp;€</div>
            </div>
        </div>
    </a>
</li>
'''

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the desired element
price_element = soup.find('div', class_='body-2 shrink-0 pt-4 text-left text-action-default-low')

# Extract the price
price = price_element.text.strip()

print(price)
