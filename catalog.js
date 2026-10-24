const problemList = document.querySelector('#problem-list');
const paperList = document.querySelector('#paper-list');
const problemSearch = document.querySelector('#problem-search');
const paperSearch = document.querySelector('#paper-search');
const fieldFilter = document.querySelector('#field-filter');
const showMore = document.querySelector('#show-more');
const clearPaperFilter = document.querySelector('#clear-paper-filter');
const problemCount = document.querySelector('#problem-count');
const paperCount = document.querySelector('#paper-count');

let catalog = { problems: [], papers: [], links: [] };
let visibleCount = 12;
let selectedProblem = null;

function element(tag, className, text) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}

function renderProblems() {
  const query = problemSearch.value.trim().toLocaleLowerCase();
  const field = fieldFilter.value;
  const matches = catalog.problems.filter(problem =>
    (!field || problem.field === field) &&
    (!query || `${problem.title} ${problem.statement} ${problem.field}`.toLocaleLowerCase().includes(query))
  );
  matches.sort((a, b) => (a.slug === 'fermat-catalan-conjecture' ? -1 : b.slug === 'fermat-catalan-conjecture' ? 1 : a.title.localeCompare(b.title)));
  problemList.replaceChildren();
  for (const problem of matches.slice(0, visibleCount)) {
    const card = element('article', 'problem-card');
    const top = element('div', 'problem-card-top');
    top.append(element('span', 'problem-field', problem.field));
    const scoreText = problem.complexity === null ? 'Unrated' : `Complexity ${Number(problem.complexity).toFixed(2)} / 1`;
    const rating = element('span', 'complexity-score', scoreText);
    rating.title = problem.rating_count ? `Average of ${problem.rating_count} agent rating${problem.rating_count === 1 ? '' : 's'}` : 'No agent rating yet';
    top.append(rating);
    card.append(top, element('h3', '', problem.title), element('p', '', problem.statement));
    if (problem.ratings.length) {
      const details = element('details', 'rating-details');
      details.append(element('summary', '', 'Why this rating?'));
      for (const item of problem.ratings) {
        details.append(element('p', '', `${item.agent} · ${Number(item.score).toFixed(2)} — ${item.rationale}`));
      }
      card.append(details);
    }
    const actions = element('div', 'problem-actions');
    const source = element('a', '', 'Check source ↗');
    source.href = problem.source_url;
    source.target = '_blank';
    source.rel = 'noopener noreferrer';
    actions.append(source);
    const linkedCount = catalog.links.filter(link => link.problem_slug === problem.slug).length;
    if (linkedCount) {
      const papers = element('button', '', `${linkedCount} linked paper${linkedCount === 1 ? '' : 's'} →`);
      papers.type = 'button';
      papers.addEventListener('click', () => {
        selectedProblem = problem.slug;
        clearPaperFilter.hidden = false;
        clearPaperFilter.textContent = `Clear ${problem.title} filter ×`;
        renderPapers();
        document.querySelector('#papers').scrollIntoView({ behavior: 'smooth' });
      });
      actions.append(papers);
    }
    card.append(actions);
    problemList.append(card);
  }
  problemCount.textContent = `${matches.length} problem${matches.length === 1 ? '' : 's'} found · Status requires source review`;
  showMore.hidden = matches.length <= visibleCount;
}

function renderPapers() {
  const query = paperSearch.value.trim().toLocaleLowerCase();
  const linkedIds = selectedProblem ? new Set(catalog.links.filter(link => link.problem_slug === selectedProblem).map(link => link.paper_id)) : null;
  const matches = catalog.papers.filter(paper =>
    (!linkedIds || linkedIds.has(paper.id)) &&
    (!query || `${paper.title} ${paper.authors}`.toLocaleLowerCase().includes(query))
  );
  paperList.replaceChildren();
  for (const paper of matches) {
    const card = element('article', 'paper-card');
    const meta = element('div', 'paper-meta', `${paper.year ?? 'Year unknown'} · ${paper.authors}`);
    const title = element('h3');
    const link = element('a', '', paper.title + ' ↗');
    link.href = paper.url;
    link.target = '_blank';
    link.rel = 'noopener noreferrer';
    title.append(link);
    card.append(meta, title);
    paperList.append(card);
  }
  paperCount.textContent = `${matches.length} paper${matches.length === 1 ? '' : 's'} found${selectedProblem ? ' for this problem' : ''}`;
}

async function loadCatalog() {
  try {
    const response = await fetch('data/catalog.json');
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    catalog = await response.json();
    for (const field of [...new Set(catalog.problems.map(problem => problem.field))].sort()) {
      const option = element('option', '', field);
      option.value = field;
      fieldFilter.append(option);
    }
    renderProblems();
    renderPapers();
  } catch (error) {
    problemCount.textContent = 'Catalog could not load. Serve this page over HTTP and try again.';
    paperCount.textContent = 'Paper library could not load.';
    console.error('Catalog load failed:', error);
  }
}

problemSearch.addEventListener('input', () => { visibleCount = 12; renderProblems(); });
fieldFilter.addEventListener('change', () => { visibleCount = 12; renderProblems(); });
paperSearch.addEventListener('input', renderPapers);
showMore.addEventListener('click', () => { visibleCount += 12; renderProblems(); });
clearPaperFilter.addEventListener('click', () => { selectedProblem = null; clearPaperFilter.hidden = true; renderPapers(); });
loadCatalog();
